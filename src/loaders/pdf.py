from langchain_core.documents import Document

from .base import BaseLoader
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader, PyMuPDFLoader


class SimplePDFLoader(BaseLoader):

    def load(self, path: Path) -> list[Document]:
        path = Path(path)
        loader = PyPDFLoader(
            file_path=path
        )
        return loader.load()

class ComplexPDFLoader(BaseLoader):

    def load(self, path: Path) -> list[Document]:
        path = Path(path)
        loader = PyMuPDFLoader(file_path=path)
        return loader.load()