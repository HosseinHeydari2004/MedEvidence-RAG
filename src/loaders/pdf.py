from pathlib import Path

from langchain_core.documents import Document
from langchain_community.document_loaders import PyMuPDFLoader

from unstructured.documents.elements import (
    Title,
    Table,
    ListItem,
    NarrativeText,
)
from unstructured.partition.auto import partition

from .base import BaseLoader


class SimplePDFLoader(BaseLoader):
    """
    Lightweight PDF loader for simple text-based PDF documents.
    """

    def load(self, path: Path | str) -> list[Document]:
        path = Path(path)

        loader = PyMuPDFLoader(
            file_path=path
        )

        return loader.load()
