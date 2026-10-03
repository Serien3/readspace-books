#!/usr/bin/env python3
"""下载 EWD249 原始 HTML，并转换成保留内容结构的 Markdown。

只需要 Python 3，无需安装依赖：
    python download_ewd249.py
    python download_ewd249.py --output-dir ./ewd249

也可转换已经下载的 HTML（默认仍会下载插图）：
    python download_ewd249.py --input ./EWD249.html
    python download_ewd249.py --input ./EWD249.html --no-images

输出目录中包含原始 EWD249.html、EWD249.md 及四幅插图。
Markdown 保留原文，不翻译、不摘要；复杂公式、程序块、上下标和
下划线使用 Markdown 允许的内嵌 HTML，以保留原有含义与缩进。
建议用支持内嵌 HTML 的 Markdown 阅读器打开。
"""

import argparse
import html
import re
import sys
from dataclasses import dataclass, field
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlsplit
from urllib.request import Request, urlopen


SOURCE_URL = (
    "https://www.cs.utexas.edu/~EWD/transcriptions/"
    "EWD02xx/EWD249/EWD249.html"
)
VOID_TAGS = {"br", "hr", "img", "meta", "link", "input", "wbr"}


@dataclass
class Node:
    tag: str
    attrs: dict = field(default_factory=dict)
    children: list = field(default_factory=list)


class DocumentParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node("root")
        self.stack = [self.root]

    def handle_starttag(self, tag, attrs):
        node = Node(tag, dict(attrs))
        self.stack[-1].children.append(node)
        if tag not in VOID_TAGS:
            self.stack.append(node)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID_TAGS:
            self.handle_endtag(tag)

    def handle_endtag(self, tag):
        for index in range(len(self.stack) - 1, 0, -1):
            if self.stack[index].tag == tag:
                del self.stack[index:]
                break

    def handle_data(self, data):
        self.stack[-1].children.append(data)


def nodes(node):
    if isinstance(node, Node):
        yield node
        for child in node.children:
            yield from nodes(child)


def plain(node):
    if isinstance(node, str):
        return node
    if node.tag == "br":
        return "\n"
    return "".join(plain(child) for child in node.children)


def compact(text):
    return re.sub(r"\s+", " ", text).strip()


def escape_markdown(text):
    text = re.sub(r"\s+", " ", text)
    text = html.escape(text, quote=False)
    return re.sub(r"([\\`*_\[\]#|])", r"\\\1", text)


def fetch(url):
    request = Request(url, headers={"User-Agent": "EWD249-local-converter/1.0"})
    with urlopen(request, timeout=60) as response:
        data = response.read()
        content_type = response.headers.get("Content-Type", "")
    if not data:
        raise ValueError("下载内容为空：" + url)
    return data, content_type


class MarkdownConverter:
    def __init__(self, body, image_paths):
        self.image_paths = image_paths
        tables = [node for node in nodes(body) if node.tag == "table"]
        # 原网页目录各行的首列为页码，末列为章节名。
        self.headings = set()
        self.toc = None
        for table in tables:
            rows = [node for node in nodes(table) if node.tag == "tr"]
            cells = [[c for c in row.children
                      if isinstance(c, Node) and c.tag in {"td", "th"}]
                     for row in rows]
            if len(cells) > 1 and all(
                row and compact(plain(row[0])).isdigit() for row in cells
            ):
                self.toc = table
                self.headings.update(compact(plain(row[-1])) for row in cells)

    def raw(self, node):
        if isinstance(node, str):
            return html.escape(node, quote=False)
        if node.tag in {"script", "style", "head"}:
            return ""
        if node.tag in {"font", "csobj", "span", "center", "div"}:
            return "".join(self.raw(c) for c in node.children)
        attrs = []
        for key, value in node.attrs.items():
            if key not in {"href", "src", "alt", "title", "colspan", "rowspan"}:
                continue
            value = value or ""
            if key == "src":
                value = self.image_paths.get(value, urljoin(SOURCE_URL, value))
            elif key == "href":
                value = urljoin(SOURCE_URL, value)
            attrs.append(f' {key}="{html.escape(value, quote=True)}"')
        start = "<" + node.tag + "".join(attrs) + ">"
        if node.tag in VOID_TAGS:
            return start
        return start + "".join(self.raw(c) for c in node.children) + f"</{node.tag}>"

    def inline(self, node):
        if isinstance(node, str):
            return escape_markdown(node)
        inner = "".join(self.inline(c) for c in node.children)
        if node.tag in {"sub", "sup", "u"}:
            return self.raw(node)
        if node.tag == "br":
            return "<br>"
        if node.tag in {"i", "em"}:
            return "*" + inner.strip() + "*"
        if node.tag in {"b", "strong"}:
            return "**" + inner.strip() + "**"
        if node.tag == "a":
            target = urljoin(SOURCE_URL, node.attrs.get("href", ""))
            return "[" + inner.strip() + "](<" + target + ">)"
        if node.tag == "img":
            source = node.attrs.get("src", "")
            target = self.image_paths.get(source, urljoin(SOURCE_URL, source))
            alt = node.attrs.get("alt") or Path(urlsplit(source).path).stem
            return "![" + escape_markdown(alt) + "](<" + target + ">)"
        return inner

    def block(self, node):
        if isinstance(node, str):
            return self.inline(node) if node.strip() else ""
        if node.tag in {"head", "script", "style"}:
            return ""
        if node.tag == "hr":
            return "\n\n---\n\n"
        if node.tag == "br":
            return "\n"
        if node.tag == "blockquote":
            # 保留原程序/公式中的空格、换行、下划线及上下标。
            return "\n\n" + self.raw(node) + "\n\n"
        if node.tag == "table":
            if node is self.toc:
                lines = ["| Page | Section |", "| ---: | --- |"]
                for row in nodes(node):
                    if row.tag != "tr":
                        continue
                    cells = [c for c in row.children
                             if isinstance(c, Node) and c.tag in {"td", "th"}]
                    if cells:
                        lines.append("| " + self.inline(cells[0]).strip() + " | "
                                     + self.inline(cells[-1]).strip() + " |")
                return "\n\n" + "\n".join(lines) + "\n\n"
            return "\n\n" + self.raw(node) + "\n\n"
        if node.tag == "p":
            label = compact(plain(node))
            if not label:
                return ""
            if label in self.headings or label == "Table of contents.":
                return "\n\n## " + escape_markdown(label) + "\n\n"
            if label.isupper() and len(label) > 10:
                return "\n\n# " + escape_markdown(label) + "\n\n"
            return "\n\n" + self.inline(node).strip() + "\n\n"
        if node.tag in {"root", "html", "body", "div", "center"}:
            return "".join(self.block(c) for c in node.children)
        return self.inline(node)

    def convert(self, body):
        result = self.block(body)
        # 不全局折叠空行，避免改写内嵌 HTML 中的程序布局。
        return result.strip() + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--output-dir", type=Path, default=Path("ewd249"))
    parser.add_argument("--input", type=Path, help="已经下载的 HTML 文件")
    parser.add_argument("--no-images", action="store_true", help="不下载插图，保留在线图片链接")
    args = parser.parse_args()

    if args.input:
        source = args.input.read_bytes()
    else:
        source, content_type = fetch(SOURCE_URL)
        if "html" not in content_type.lower():
            raise ValueError("服务器未返回 HTML：" + content_type)

    document = DocumentParser()
    document.feed(source.decode("utf-8-sig"))
    body = next((n for n in nodes(document.root) if n.tag == "body"), None)
    if body is None or not any(n.attrs.get("id") == "content" for n in nodes(body)):
        raise ValueError("未找到 EWD249 正文，请检查下载内容或网页结构变化。")

    args.output_dir.mkdir(parents=True, exist_ok=True)
    html_path = args.output_dir / "EWD249.html"
    html_path.write_bytes(source)
    image_paths = {}
    for node in nodes(body):
        if node.tag != "img" or not node.attrs.get("src"):
            continue
        source_url = node.attrs["src"]
        if source_url in image_paths:
            continue
        if args.no_images:
            image_paths[source_url] = urljoin(SOURCE_URL, source_url)
            continue
        name = Path(urlsplit(source_url).path).name
        data, content_type = fetch(urljoin(SOURCE_URL, source_url))
        if not content_type.lower().startswith("image/"):
            raise ValueError("服务器未返回图片：" + source_url)
        (args.output_dir / name).write_bytes(data)
        image_paths[source_url] = name

    converter = MarkdownConverter(body, image_paths)
    markdown_path = args.output_dir / "EWD249.md"
    markdown_path.write_text(converter.convert(body), encoding="utf-8")
    print("HTML：", html_path.resolve())
    print("Markdown：", markdown_path.resolve())
    print("插图：", len(image_paths), "幅" + ("（在线链接）" if args.no_images else "（本地文件）"))


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, UnicodeError) as error:
        print("失败：" + str(error), file=sys.stderr)
        sys.exit(1)
