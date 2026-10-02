from pathlib import Path

from langchain_core.documents import Document
from langchain_community.document_loaders import PyMuPDFLoader

from .base import BaseLoader


class PDFLoader(BaseLoader):
    """
    Lightweight PDF loader for  text-based PDF documents.
    """

    def load(self, path: Path | str) -> list[Document]:
        path = Path(path)

        loader = PyMuPDFLoader(
            file_path=path
        )

        return loader.load()
