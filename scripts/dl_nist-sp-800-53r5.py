#!/usr/bin/env python3
"""
Generate docs/_data/nist-sp-800-53r5.yml from the NIST SP 800-53r5 PDF.

Approach:
1. Download the PDF if it is not cached locally.
2. Reuse the PDF outline in the THE CONTROLS section for deep links.
3. Read only the controls-section page range with pypdf.
4. Extract base control headings from page text, requiring nearby Control: text.
5. Warn if controls within a family are not consecutive.
"""

from __future__ import annotations

import argparse
import json
import logging
import re
import urllib.parse
from collections import OrderedDict, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Optional

import requests
import yaml
from pypdf import PdfReader

SCRIPT_DIR = Path(__file__).parent
PDF_URL = "https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf"
PDF_DIR = (SCRIPT_DIR / ".." / "_refs-markdown" / "nist-sp-800-53r5").resolve()
PDF_PATH = PDF_DIR / "NIST.SP.800-53r5.pdf"
YAML_PATH = (SCRIPT_DIR / ".." / "docs" / "_data" / "nist-sp-800-53r5.yml").resolve()

# Base controls only. Enhancements like AC-2(1) are intentionally excluded.
CONTROL_SAME_LINE_RE = re.compile(r"^([A-Z]{2,3}-\d{1,3})\s+(.+?)\s*$")
CONTROL_CODE_ONLY_RE = re.compile(r"^([A-Z]{2,3}-\d{1,3})\s*$")
TITLE_LINE_RE = re.compile(r"^[A-Z][A-Z0-9\s,&/\-]+$")


@dataclass(frozen=True)
class ControlEntry:
    code: str
    title: str
    page: int
    url: str

    @property
    def key(self) -> str:
        return self.code.lower()

    @property
    def family(self) -> str:
        return self.code.split("-", 1)[0]

    @property
    def number(self) -> int:
        return int(self.code.split("-", 1)[1])


@dataclass(frozen=True)
class BookmarkInfo:
    title: str
    page: Optional[int] = None
    level: int = 0
    x_coord: Optional[float] = None
    y_coord: Optional[float] = None
    zoom: Optional[float] = None
    obj_num: Optional[int] = None
    obj_gen: Optional[int] = None

    @property
    def has_coordinates(self) -> bool:
        return self.x_coord is not None and self.y_coord is not None

    @property
    def has_object_reference(self) -> bool:
        return self.obj_num is not None


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--force-download",
        action="store_true",
        help="Re-download the PDF even if it is already cached",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit non-zero if a control family has numbering gaps",
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Enable debug logging",
    )
    return parser.parse_args()


def setup_logging(debug: bool) -> None:
    logging.basicConfig(
        level=logging.DEBUG if debug else logging.INFO,
        format="%(levelname)s: %(message)s",
    )


def download_pdf(force_download: bool) -> Path:
    PDF_DIR.mkdir(parents=True, exist_ok=True)
    if PDF_PATH.exists() and not force_download:
        logging.info("Using cached PDF: %s", PDF_PATH)
        return PDF_PATH

    logging.info("Downloading PDF: %s", PDF_URL)
    response = requests.get(PDF_URL, stream=True, timeout=30)
    response.raise_for_status()

    with PDF_PATH.open("wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

    logging.info("Saved PDF: %s", PDF_PATH)
    return PDF_PATH


def normalize_title(raw_title: str) -> str:
    acronyms = {
        "AC",
        "AT",
        "AU",
        "CA",
        "CM",
        "CP",
        "IA",
        "IR",
        "MA",
        "MP",
        "PE",
        "PL",
        "PM",
        "PS",
        "PT",
        "RA",
        "SA",
        "SC",
        "SI",
        "SR",
        "AI",
        "API",
        "DNS",
        "GAI",
        "HTTP",
        "HTTPS",
        "IP",
        "IT",
        "ML",
        "OS",
        "PII",
        "PKI",
        "POA&M",
        "SQL",
        "SSL",
        "TCP",
        "TLS",
        "VPN",
    }
    lower_words = {"a", "an", "and", "as", "at", "for", "in", "of", "on", "or", "the", "to", "with"}
    words = raw_title.split()
    normalized = []
    for index, word in enumerate(words):
        bare = "".join(ch for ch in word if ch.isalnum())
        if bare.upper() in acronyms:
            normalized.append(word.upper())
        elif index > 0 and bare.lower() in lower_words:
            normalized.append(word.lower())
        elif bare.isalpha() and len(bare) > 1:
            normalized.append(word.capitalize())
        else:
            normalized.append(word)
    return " ".join(normalized)


def is_section_title(line: str) -> bool:
    return bool(TITLE_LINE_RE.match(line))


def has_control_marker(lines: list[str], start_index: int) -> bool:
    for candidate in lines[start_index : start_index + 8]:
        if not candidate:
            continue
        if candidate.lower().startswith("control:"):
            return True
        if CONTROL_SAME_LINE_RE.match(candidate) or CONTROL_CODE_ONLY_RE.match(candidate):
            return False
    return False


def find_title_after_code(lines: list[str], start_index: int) -> str | None:
    parts: list[str] = []
    for candidate in lines[start_index : start_index + 6]:
        if not candidate:
            continue
        lower = candidate.lower()
        if lower.startswith("control:"):
            break
        if CONTROL_CODE_ONLY_RE.match(candidate):
            break
        if re.match(r"^[a-z]\.", candidate):
            break
        if re.match(r"^\d+\.", candidate):
            break
        if is_section_title(candidate):
            parts.append(candidate)
            continue
        break
    if not parts:
        return None
    return " ".join(parts)


def filter_bookmarks_by_section(
    bookmarks: list[BookmarkInfo], section_title: str
) -> list[BookmarkInfo]:
    filtered: list[BookmarkInfo] = []
    in_target_section = False
    target_level: int | None = None

    for bookmark in bookmarks:
        if in_target_section:
            if bookmark.level > target_level:
                filtered.append(bookmark)
            else:
                break
        elif section_title.upper() in bookmark.title.upper():
            in_target_section = True
            target_level = bookmark.level
            filtered.append(bookmark)

    return filtered


def extract_bookmarks(reader: PdfReader) -> list[BookmarkInfo]:
    if not reader.outline:
        return []
    return _extract_bookmark_recursive(reader.outline, reader)


def _extract_bookmark_recursive(
    outline_items: object, reader: PdfReader, level: int = 0
) -> list[BookmarkInfo]:
    bookmarks: list[BookmarkInfo] = []
    if not isinstance(outline_items, list):
        outline_items = [outline_items]

    for outline_item in outline_items:
        bookmark = _extract_bookmark_info(outline_item, reader, level)
        if bookmark:
            bookmarks.append(bookmark)

        children = None
        if hasattr(outline_item, "children") and outline_item.children:
            children = outline_item.children
        elif isinstance(outline_item, list):
            children = outline_item

        if children:
            if hasattr(children, "__iter__") and not isinstance(children, (str, bytes)):
                children_list = list(children)
                if children_list:
                    bookmarks.extend(_extract_bookmark_recursive(children_list, reader, level + 1))
            else:
                bookmarks.extend(_extract_bookmark_recursive([children], reader, level + 1))

    return bookmarks


def _extract_bookmark_info(
    outline_item: object, reader: PdfReader, level: int
) -> BookmarkInfo | None:
    if not hasattr(outline_item, "title"):
        return None

    bookmark = BookmarkInfo(title=str(outline_item.title).strip(), level=level)
    page = None
    obj_num = None
    obj_gen = None
    x_coord = None
    y_coord = None
    zoom = None

    try:
        if "/Page" in outline_item:
            page_ref = outline_item["/Page"]
            if hasattr(page_ref, "idnum") and hasattr(page_ref, "generation"):
                obj_num = page_ref.idnum
                obj_gen = page_ref.generation
            elif hasattr(page_ref, "indirect_reference"):
                ref = page_ref.indirect_reference
                if hasattr(ref, "idnum") and hasattr(ref, "generation"):
                    obj_num = ref.idnum
                    obj_gen = ref.generation

            for page_idx, candidate in enumerate(reader.pages):
                if candidate == page_ref:
                    page = page_idx + 1
                    break

        if hasattr(outline_item, "node") and outline_item.node and "/D" in outline_item.node:
            dest_array = outline_item.node["/D"]
            if isinstance(dest_array, list) and len(dest_array) >= 4:
                if dest_array[1] == "/XYZ":
                    x_coord = float(dest_array[2]) if dest_array[2] is not None else None
                    y_coord = float(dest_array[3]) if dest_array[3] is not None else None
                    if len(dest_array) >= 5 and dest_array[4] is not None:
                        zoom = float(dest_array[4])
                elif dest_array[1] == "/FitH" and len(dest_array) >= 3:
                    y_coord = float(dest_array[2]) if dest_array[2] is not None else None

        if x_coord is None and "/Left" in outline_item:
            x_coord = float(outline_item["/Left"])
        if y_coord is None and "/Top" in outline_item:
            y_coord = float(outline_item["/Top"])
    except Exception:
        pass

    return BookmarkInfo(
        title=bookmark.title,
        page=page,
        level=bookmark.level,
        x_coord=x_coord,
        y_coord=y_coord,
        zoom=zoom,
        obj_num=obj_num,
        obj_gen=obj_gen,
    )


def build_bookmark_url(bookmark: BookmarkInfo) -> str:
    if not bookmark.page:
        return PDF_URL
    if bookmark.has_object_reference and bookmark.has_coordinates:
        dest_array = [
            {"num": bookmark.obj_num, "gen": bookmark.obj_gen or 0},
            {"name": "XYZ"},
            bookmark.x_coord,
            bookmark.y_coord,
            bookmark.zoom or 0,
        ]
        return f"{PDF_URL}#{urllib.parse.quote(json.dumps(dest_array, separators=(',', ':')))}"
    if bookmark.has_coordinates:
        page_url = f"{PDF_URL}#page={bookmark.page}"
        if bookmark.x_coord is not None and bookmark.y_coord is not None:
            zoom_param = f",{bookmark.zoom:.2f}" if bookmark.zoom else ",null"
            return f"{page_url}&view=XYZ,{bookmark.x_coord:.1f},{bookmark.y_coord:.1f}{zoom_param}"
        return f"{page_url}&view=FitH,{bookmark.y_coord:.1f}"
    return build_url(bookmark.page)


def bookmark_key(title: str) -> str | None:
    match = re.match(r"^([A-Z]{2,3}-\d{1,3})(?:\s+.+)?$", title.strip())
    if not match:
        return None
    return match.group(1).lower()


def extract_controls(reader: PdfReader) -> OrderedDict[str, ControlEntry]:
    controls_bookmarks = extract_controls_section_bookmarks(reader)
    bookmark_urls = extract_bookmark_urls(controls_bookmarks)
    bookmark_titles = extract_bookmark_titles(controls_bookmarks)
    text_controls = extract_controls_from_text(reader, controls_bookmarks)

    controls: OrderedDict[str, ControlEntry] = OrderedDict()
    all_keys = sorted(set(bookmark_urls) | set(text_controls))
    for key in all_keys:
        code = key.upper()
        page = extract_bookmark_page(controls_bookmarks, key) or text_controls.get(key, {}).get("page") or 1
        title = (
            text_controls.get(key, {}).get("title")
            or bookmark_titles.get(key)
            or code
        )
        controls[code] = ControlEntry(
            code=code,
            title=title.removeprefix(f"{code} ").strip(),
            page=int(page),
            url=bookmark_urls.get(key, build_url(int(page))),
        )

    return controls


def extract_controls_from_text(
    reader: PdfReader, controls_bookmarks: list[BookmarkInfo]
) -> dict[str, dict[str, str | int]]:
    controls: dict[str, dict[str, str | int]] = {}
    control_pages = sorted({bookmark.page for bookmark in controls_bookmarks if bookmark.page})
    if control_pages:
        page_range = range(control_pages[0], control_pages[-1] + 1)
    else:
        page_range = range(1, len(reader.pages) + 1)

    for page_index in page_range:
        page = reader.pages[page_index - 1]
        text = page.extract_text() or ""
        lines = [line.strip() for line in text.splitlines()]

        for i, line in enumerate(lines):
            same_line = CONTROL_SAME_LINE_RE.match(line)
            if same_line:
                code = same_line.group(1).lower()
                if code not in controls and has_control_marker(lines, i + 1):
                    title_tail = same_line.group(2)
                    continuation = find_title_after_code(lines, i + 1)
                    if continuation:
                        title_tail = f"{title_tail} {continuation}"
                    controls[code] = {
                        "title": f"{code.upper()} {normalize_title(title_tail)}",
                        "page": page_index,
                    }
                continue

            code_only = CONTROL_CODE_ONLY_RE.match(line)
            if not code_only:
                continue

            code = code_only.group(1).lower()
            if code in controls:
                continue

            raw_title = find_title_after_code(lines, i + 1)
            if not raw_title or not has_control_marker(lines, i + 1):
                logging.debug("Skipping code-only match without title: %s on page %s", code, page_index)
                continue

            controls[code] = {
                "title": f"{code.upper()} {normalize_title(raw_title)}",
                "page": page_index,
            }

    return controls


def extract_controls_section_bookmarks(reader: PdfReader) -> list[BookmarkInfo]:
    return filter_bookmarks_by_section(extract_bookmarks(reader), "THE CONTROLS")


def extract_bookmark_urls(bookmarks: Iterable[BookmarkInfo]) -> dict[str, str]:
    urls: dict[str, str] = {}
    for bookmark in bookmarks:
        key = bookmark_key(bookmark.title)
        if not key or key in urls:
            continue
        urls[key] = build_bookmark_url(bookmark)
    return urls


def extract_bookmark_titles(bookmarks: Iterable[BookmarkInfo]) -> dict[str, str]:
    titles: dict[str, str] = {}
    for bookmark in bookmarks:
        key = bookmark_key(bookmark.title)
        if not key or key in titles:
            continue
        titles[key] = normalize_title(bookmark.title)
    return titles


def extract_bookmark_page(bookmarks: Iterable[BookmarkInfo], key: str) -> int | None:
    for bookmark in bookmarks:
        if bookmark_key(bookmark.title) == key:
            return bookmark.page
    return None


def build_url(page: int) -> str:
    return f"{PDF_URL}#page={page}"


def generate_yaml(controls: Iterable[ControlEntry]) -> str:
    data: OrderedDict[str, dict[str, str]] = OrderedDict()
    for control in sorted(controls, key=sort_key):
        data[control.key] = {
            "title": f"{control.code} {control.title}",
            "url": control.url,
        }

    content = "# NIST NIST-SP-800-53R5\n"
    content += f"# Generated from {PDF_URL}\n\n"
    content += yaml.dump(dict(data), default_flow_style=False, sort_keys=False, allow_unicode=True)
    return content


def check_consecutive(controls: Iterable[ControlEntry]) -> list[str]:
    grouped: dict[str, list[int]] = defaultdict(list)
    for control in controls:
        grouped[control.family].append(control.number)

    warnings: list[str] = []
    for family in sorted(grouped):
        numbers = sorted(set(grouped[family]))
        for current, nxt in zip(numbers, numbers[1:]):
            if nxt != current + 1:
                warnings.append(f"{family}: missing {current + 1} between {current} and {nxt}")
    return warnings


def sort_key(control: ControlEntry) -> tuple[str, int]:
    return (control.family, control.number)


def write_yaml(content: str) -> Path:
    YAML_PATH.parent.mkdir(parents=True, exist_ok=True)
    YAML_PATH.write_text(content, encoding="utf-8")
    logging.info("Wrote YAML: %s", YAML_PATH)
    return YAML_PATH


def main() -> None:
    args = parse_args()
    setup_logging(args.debug)

    pdf_path = download_pdf(args.force_download)
    reader = PdfReader(str(pdf_path))
    logging.info("Loaded PDF with %s pages", len(reader.pages))

    controls = extract_controls(reader)
    logging.info("Extracted %s controls", len(controls))

    warnings = check_consecutive(controls.values())
    for warning in warnings:
        logging.warning("Consecutiveness check: %s", warning)

    write_yaml(generate_yaml(controls.values()))

    if args.strict and warnings:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
