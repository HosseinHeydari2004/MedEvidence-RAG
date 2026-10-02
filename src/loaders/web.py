from pathlib import Path
from .base import BaseLoader
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.documents import Document
from typing import Union, Sequence
from dotenv import load_dotenv

load_dotenv()

class WebLoader(BaseLoader):

    def load(self, urls:Union[str, Sequence[str]]) -> list[Document]:
        loader = WebBaseLoader(
            web_path=urls,
            show_progress=True,
            raise_for_status=True,
            requests_per_second=3
        )
        return loader.load()