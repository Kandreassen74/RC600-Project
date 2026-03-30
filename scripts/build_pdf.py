#!/usr/bin/env python3
"""Generate a simple PDF from docs/rc600_praktisk_bruk.md without external dependencies."""
from pathlib import Path

SOURCE = Path("docs/rc600_praktisk_bruk.md")
TARGET = Path("docs/RC600-praktisk-guide.pdf")

PAGE_WIDTH = 595
PAGE_HEIGHT = 842
MARGIN_X = 48
MARGIN_Y = 52
FONT_SIZE = 11
LEADING = 15
MAX_CHARS = 88


def escape_pdf_text(value: str) -> str:
    return value.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


def wrap_line(line: str, width: int):
    if not line:
        return [""]
    words = line.split(" ")
    rows = []
    current = ""
    for word in words:
        candidate = word if not current else f"{current} {word}"
        if len(candidate) <= width:
            current = candidate
        else:
            rows.append(current)
            current = word
    if current:
        rows.append(current)
    return rows


def markdown_to_text_lines(raw: str):
    lines = []
    for original in raw.splitlines():
        line = original.rstrip()
        if line.startswith("#"):
            line = line.lstrip("#").strip().upper()
        elif line.startswith("- "):
            line = "• " + line[2:]

        if len(line) <= MAX_CHARS:
            lines.append(line)
        else:
            lines.extend(wrap_line(line, MAX_CHARS))
    return lines


def paginate(lines):
    content_height = PAGE_HEIGHT - (2 * MARGIN_Y)
    per_page = max(1, content_height // LEADING)
    pages = []
    for idx in range(0, len(lines), per_page):
        pages.append(lines[idx : idx + per_page])
    return pages


def build_stream(page_lines):
    y = PAGE_HEIGHT - MARGIN_Y
    chunks = ["BT", f"/F1 {FONT_SIZE} Tf", f"1 0 0 1 {MARGIN_X} {y} Tm"]
    first = True
    for line in page_lines:
        text = escape_pdf_text(line)
        if first:
            chunks.append(f"({text}) Tj")
            first = False
        else:
            chunks.append(f"0 -{LEADING} Td ({text}) Tj")
    chunks.append("ET")
    return "\n".join(chunks) + "\n"


def build_pdf(pages):
    objects = []

    def add_object(body: str) -> int:
        objects.append(body)
        return len(objects)

    catalog_id = add_object("<< /Type /Catalog /Pages 2 0 R >>")
    pages_placeholder_id = add_object("<< /Type /Pages /Kids [] /Count 0 >>")
    font_id = add_object("<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>")

    page_ids = []
    for page in pages:
        stream = build_stream(page)
        stream_id = add_object(
            f"<< /Length {len(stream.encode('utf-8'))} >>\nstream\n{stream}endstream"
        )
        page_id = add_object(
            "<< /Type /Page "
            f"/Parent {pages_placeholder_id} 0 R "
            f"/MediaBox [0 0 {PAGE_WIDTH} {PAGE_HEIGHT}] "
            f"/Resources << /Font << /F1 {font_id} 0 R >> >> "
            f"/Contents {stream_id} 0 R >>"
        )
        page_ids.append(page_id)

    kids = " ".join(f"{pid} 0 R" for pid in page_ids)
    objects[pages_placeholder_id - 1] = (
        f"<< /Type /Pages /Kids [{kids}] /Count {len(page_ids)} >>"
    )

    output = ["%PDF-1.4\n"]
    offsets = [0]
    for i, obj in enumerate(objects, start=1):
        offsets.append(sum(len(part.encode("utf-8")) for part in output))
        output.append(f"{i} 0 obj\n{obj}\nendobj\n")

    xref_start = sum(len(part.encode("utf-8")) for part in output)
    output.append(f"xref\n0 {len(objects) + 1}\n")
    output.append("0000000000 65535 f \n")
    for off in offsets[1:]:
        output.append(f"{off:010d} 00000 n \n")

    output.append(
        "trailer\n"
        f"<< /Size {len(objects) + 1} /Root {catalog_id} 0 R >>\n"
        f"startxref\n{xref_start}\n%%EOF\n"
    )
    return "".join(output).encode("utf-8")


def main():
    raw = SOURCE.read_text(encoding="utf-8")
    lines = markdown_to_text_lines(raw)
    pages = paginate(lines)
    pdf_bytes = build_pdf(pages)
    TARGET.write_bytes(pdf_bytes)
    print(f"Wrote {TARGET} ({len(pdf_bytes)} bytes, {len(pages)} pages)")


if __name__ == "__main__":
    main()
