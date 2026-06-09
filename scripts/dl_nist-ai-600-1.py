#!/usr/bin/env python3
"""
Generate docs/_data/nist-ai-600-1.yml from the NIST AI 600-1 PDF.

This is the dedicated AI-600-1 generator extracted from the former shared
NIST script. It keeps the existing bookmark-based deep-link behavior and the
AI-specific leaf extraction logic.
"""

from __future__ import annotations

import argparse
import json
import logging
import re
import urllib.parse
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Union

import requests
import yaml
from pypdf import PdfReader

SCRIPT_DIR = Path(__file__).parent


@dataclass
class BookmarkInfo:
    """Represents a PDF bookmark with navigation metadata."""

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


@dataclass
class Config:
    filename_prefix: str = "NIST.AI.600-1"
    section_filter: str = "ALL"
    force_download: bool = False
    debug: bool = False
    title_case: bool = False
    ignore_anonymous_sections: bool = True
    leafs: bool = False
    leafs_section: str = "2. Overview of Risks Unique to or Exacerbated by GAI"

    @property
    def document_type(self) -> str:
        return self.filename_prefix.lower().replace(".", "-")

    @property
    def pdf_url(self) -> str:
        return f"https://nvlpubs.nist.gov/nistpubs/ai/{self.filename_prefix}.pdf"

    @property
    def output_dir(self) -> Path:
        return (SCRIPT_DIR / ".." / "_refs-markdown" / self.document_type).resolve()

    @property
    def pdf_filename(self) -> str:
        return f"{self.filename_prefix}.pdf"

    @property
    def yaml_output_path(self) -> Path:
        return (SCRIPT_DIR / ".." / "docs" / "_data" / f"{self.document_type}.yml").resolve()


class PDFProcessor:
    def __init__(self, config: Config):
        self.config = config
        self.logger = logging.getLogger(__name__)

    def download_pdf(self) -> Path:
        pdf_path = self.config.output_dir / self.config.pdf_filename
        self.config.output_dir.mkdir(parents=True, exist_ok=True)

        if pdf_path.exists() and not self.config.force_download:
            self.logger.info("Using cached PDF: %s", pdf_path)
            return pdf_path

        self.logger.info("Downloading PDF from %s", self.config.pdf_url)
        response = requests.get(self.config.pdf_url, stream=True, timeout=30)
        response.raise_for_status()

        with pdf_path.open("wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        self.logger.info("PDF saved to %s", pdf_path)
        return pdf_path

    def load_pdf(self, pdf_path: Path) -> PdfReader:
        reader = PdfReader(str(pdf_path))
        self.logger.info("Loaded PDF with %s pages", len(reader.pages))
        return reader


class BookmarkExtractor:
    def __init__(self, config: Config):
        self.config = config
        self.logger = logging.getLogger(__name__)

    def extract_bookmarks(self, reader: PdfReader) -> List[BookmarkInfo]:
        if not reader.outline:
            self.logger.warning("No outline found in PDF")
            return []
        bookmarks = self._extract_recursive(reader.outline, reader)
        self.logger.info("Extracted %s bookmarks", len(bookmarks))
        return bookmarks

    def _extract_recursive(
        self, outline_items: Union[List, object], reader: PdfReader, level: int = 0
    ) -> List[BookmarkInfo]:
        bookmarks = []
        if not isinstance(outline_items, list):
            outline_items = [outline_items]

        for outline_item in outline_items:
            bookmark = self._extract_info(outline_item, reader, level)
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
                        bookmarks.extend(self._extract_recursive(children_list, reader, level + 1))
                else:
                    bookmarks.extend(self._extract_recursive([children], reader, level + 1))

        return bookmarks

    def _extract_info(
        self, outline_item: object, reader: PdfReader, level: int
    ) -> Optional[BookmarkInfo]:
        if not hasattr(outline_item, "title"):
            return None

        bookmark = BookmarkInfo(title=str(outline_item.title).strip(), level=level)

        try:
            if "/Page" in outline_item:
                page_ref = outline_item["/Page"]
                if hasattr(page_ref, "idnum") and hasattr(page_ref, "generation"):
                    bookmark.obj_num = page_ref.idnum
                    bookmark.obj_gen = page_ref.generation
                elif hasattr(page_ref, "indirect_reference"):
                    ref = page_ref.indirect_reference
                    if hasattr(ref, "idnum") and hasattr(ref, "generation"):
                        bookmark.obj_num = ref.idnum
                        bookmark.obj_gen = ref.generation

                for page_idx, page in enumerate(reader.pages):
                    if page == page_ref:
                        bookmark.page = page_idx + 1
                        break

            if hasattr(outline_item, "node") and outline_item.node and "/D" in outline_item.node:
                dest_array = outline_item.node["/D"]
                if isinstance(dest_array, list) and len(dest_array) >= 4:
                    if dest_array[1] == "/XYZ":
                        bookmark.x_coord = float(dest_array[2]) if dest_array[2] is not None else None
                        bookmark.y_coord = float(dest_array[3]) if dest_array[3] is not None else None
                        if len(dest_array) >= 5 and dest_array[4] is not None:
                            bookmark.zoom = float(dest_array[4])
                    elif dest_array[1] == "/FitH" and len(dest_array) >= 3:
                        bookmark.y_coord = float(dest_array[2]) if dest_array[2] is not None else None

            if bookmark.x_coord is None and "/Left" in outline_item:
                bookmark.x_coord = float(outline_item["/Left"])
            if bookmark.y_coord is None and "/Top" in outline_item:
                bookmark.y_coord = float(outline_item["/Top"])
        except Exception as exc:
            self.logger.warning("Error extracting bookmark info for '%s': %s", bookmark.title, exc)

        return bookmark


class BookmarkFilter:
    def __init__(self, config: Config):
        self.config = config
        self.logger = logging.getLogger(__name__)

    def filter_by_section(self, bookmarks: List[BookmarkInfo]) -> List[BookmarkInfo]:
        filtered = []
        in_target_section = self.config.section_filter.upper() == "ALL"
        target_level = None

        for bookmark in bookmarks:
            if self.config.ignore_anonymous_sections and self._is_anonymous_section(bookmark.title):
                continue

            if in_target_section:
                if self.config.section_filter.upper() == "ALL" or bookmark.level > target_level:
                    filtered.append(bookmark)
                else:
                    break
            else:
                if self.config.section_filter.upper() in bookmark.title.upper():
                    in_target_section = True
                    target_level = bookmark.level
                    filtered.append(bookmark)

        if self.config.leafs:
            filtered = self._filter_to_leaf_nodes(filtered)

        self.logger.info(
            "Filtered to %s bookmarks for section '%s'", len(filtered), self.config.section_filter
        )
        return filtered

    def _filter_to_leaf_nodes(self, bookmarks: List[BookmarkInfo]) -> List[BookmarkInfo]:
        leaf_bookmarks = []
        for i, bookmark in enumerate(bookmarks):
            is_leaf = True
            for next_bookmark in bookmarks[i + 1 :]:
                if next_bookmark.level > bookmark.level:
                    is_leaf = False
                    break
                if next_bookmark.level <= bookmark.level:
                    break
            if is_leaf:
                leaf_bookmarks.append(bookmark)
        return leaf_bookmarks

    def _is_anonymous_section(self, title: str) -> bool:
        return bool(re.match(r"^\s*\d+\.?\s*$", title.strip()))


class DeepLinkGenerator:
    def __init__(self, config: Config):
        self.base_url = config.pdf_url

    def create_link(self, bookmark: BookmarkInfo) -> str:
        if not bookmark.page:
            return self.base_url
        if bookmark.has_object_reference and bookmark.has_coordinates:
            dest_array = [
                {"num": bookmark.obj_num, "gen": bookmark.obj_gen or 0},
                {"name": "XYZ"},
                bookmark.x_coord,
                bookmark.y_coord,
                bookmark.zoom or 0,
            ]
            return f"{self.base_url}#{urllib.parse.quote(json.dumps(dest_array, separators=(',', ':')))}"
        if bookmark.has_coordinates:
            page_url = f"{self.base_url}#page={bookmark.page}"
            if bookmark.x_coord is not None and bookmark.y_coord is not None:
                zoom_param = f",{bookmark.zoom:.2f}" if bookmark.zoom else ",null"
                return f"{page_url}&view=XYZ,{bookmark.x_coord:.1f},{bookmark.y_coord:.1f}{zoom_param}"
            return f"{page_url}&view=FitH,{bookmark.y_coord:.1f}"
        return f"{self.base_url}#page={bookmark.page}"


class YamlGenerator:
    def __init__(self, config: Config):
        self.config = config

    def generate_yaml(
        self, bookmarks: List[BookmarkInfo], link_generator: DeepLinkGenerator
    ) -> str:
        yaml_data: Dict[str, Dict[str, str]] = {}
        for bookmark in bookmarks:
            key = self._normalize_key(bookmark.title)
            if not key:
                continue
            yaml_data[key] = {
                "title": bookmark.title,
                "url": link_generator.create_link(bookmark),
            }

        content = f"# NIST {self.config.document_type.upper()}\n"
        content += f"# Generated from {self.config.pdf_url}\n\n"
        content += yaml.dump(
            yaml_data,
            default_flow_style=False,
            sort_keys=False,
            allow_unicode=True,
            width=1000,
        )
        return content

    def _normalize_key(self, title: str) -> str:
        if match := re.match(r"^(\d+(?:\.\d+)*)\.\s*(.+)", title):
            return match.group(1).replace(".", "-")
        cleaned = re.sub(r"[^\w\s-]", "", title.lower())
        words = cleaned.split()[:3]
        return "-".join(words) if words else "item"

    def write_to_file(self, content: str) -> Path:
        self.config.yaml_output_path.parent.mkdir(parents=True, exist_ok=True)
        self.config.yaml_output_path.write_text(content, encoding="utf-8")
        logging.info("YAML written to %s", self.config.yaml_output_path)
        return self.config.yaml_output_path


class NISTAI6001Processor:
    def __init__(self, config: Config):
        self.config = config
        self.pdf_processor = PDFProcessor(config)
        self.bookmark_extractor = BookmarkExtractor(config)
        self.bookmark_filter = BookmarkFilter(config)
        self.link_generator = DeepLinkGenerator(config)
        self.yaml_generator = YamlGenerator(config)

    def process(self) -> Path:
        logging.info("Starting NIST AI 600-1 processing for section: %s", self.config.section_filter)
        pdf_path = self.pdf_processor.download_pdf()
        reader = self.pdf_processor.load_pdf(pdf_path)
        all_bookmarks = self.bookmark_extractor.extract_bookmarks(reader)
        filtered_bookmarks = self.bookmark_filter.filter_by_section(all_bookmarks)
        yaml_content = self.yaml_generator.generate_yaml(filtered_bookmarks, self.link_generator)
        return self.yaml_generator.write_to_file(yaml_content)


def parse_args() -> Config:
    parser = argparse.ArgumentParser(
        description="Extract NIST AI 600-1 bookmarks as YAML data",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        epilog="""
Examples:
  %(prog)s                            # Extract all sections from AI 600-1
  %(prog)s --section "ALL"            # Explicit full extraction
  %(prog)s --leafs                    # Extract leaf nodes from the configured AI section
  %(prog)s --force-download --debug   # Force re-download with debug
        """,
    )
    parser.add_argument(
        "--section",
        default="ALL",
        help='Section to extract. Use "ALL" for all sections',
    )
    parser.add_argument(
        "--force-download",
        action="store_true",
        help="Force re-download of PDF even if cached locally",
    )
    parser.add_argument("--debug", action="store_true", help="Enable debug logging")
    parser.add_argument(
        "--leafs",
        action="store_true",
        help="Extract only leaf nodes from the document-specific leafs section",
    )
    args = parser.parse_args()

    config = Config()
    config.section_filter = args.section
    config.force_download = args.force_download
    config.debug = args.debug
    config.leafs = args.leafs
    if config.leafs:
        config.section_filter = config.leafs_section
    return config


def setup_logging(debug: bool) -> None:
    logging.basicConfig(
        level=logging.DEBUG if debug else logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s" if debug else "%(levelname)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


def main() -> None:
    config = None
    try:
        config = parse_args()
        setup_logging(config.debug)
        output_path = NISTAI6001Processor(config).process()
        print(f"Successfully generated: {output_path}")
    except KeyboardInterrupt:
        print("\nProcessing interrupted by user")
    except Exception as exc:
        print(f"Error: {exc}")
        if config and config.debug:
            raise


if __name__ == "__main__":
    main()
