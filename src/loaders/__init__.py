from .docs import DocsLoader
from .web import WebLoader
from .csv import CsvLoader
from .text import TxtLoader
from .markdown import MarkdownLoader
from .pdf import PDFLoader

__all__ = [
    "DocsLoader",
    "WebLoader",
    "CsvLoader",
    "TxtLoader",
    "MarkdownLoader",
    "PDFLoader",
]