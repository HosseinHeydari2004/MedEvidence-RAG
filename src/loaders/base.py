from abc import ABC, abstractmethod
from typing import Literal
from pathlib import Path
from langchain_core.documents import Document
from spacy.lang import sr


class BaseLoader(ABC):
    """base loader for all loaders"""

    @abstractmethod
    def load(self, path: Path | str) -> list[Document]:
        pass
