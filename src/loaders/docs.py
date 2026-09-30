from langchain_core.documents import Document

from .base import BaseLoader
from pathlib import Path
from langchain_community.document_loaders import Docx2txtLoader


class DocsLoader(BaseLoader):
    """
    A loader for Microsoft Word documents (`.doc` / `.docx`).

    This class provides a loader for extracting content from Microsoft
    Word files. It inherits from `BaseLoader` and is intended to handle
    document files in the Word format, returning their textual content
    as a list of `Document` objects.

    Notes
    -----
    Microsoft Word documents come in two main formats:

    - `.doc`  : the legacy binary format (Word 97–2003).
    - `.docx` : the modern Office Open XML format (Word 2007+).

    Depending on the underlying parser, support for one or both formats
    may vary. For `.docx` files, loaders such as `Docx2txtLoader` or
    `UnstructuredWordDocumentLoader` are commonly used.
    """

    def load(self, path: Path | str) -> list[Document]:
        loader = Docx2txtLoader(file_path=Path(path))
        return loader.load()

