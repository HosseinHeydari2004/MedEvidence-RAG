from __future__ import annotations

import pathlib
import tempfile
import zipfile

from tqdm import tqdm
from langchain_core.documents import Document

from .base import BasePipelineLoader
from ..base import BaseLoader
from src.loaders import (
    DocsLoader,
    TxtLoader,
    PDFLoader,
    MarkdownLoader,
    CsvLoader,
)


class DocumentLoaderPipeline(BasePipelineLoader):

    def __init__(self) -> None:
        self._loaders: dict[str, type[BaseLoader]] = {
            ".docs": DocsLoader,
            ".pdf": PDFLoader,
            ".txt": TxtLoader,
            ".md": MarkdownLoader,
            ".csv": CsvLoader,
        }

    def load(
            self,
            path: pathlib.Path | str,
    ) -> list[Document]:

        if self.is_directory(path=path):
            return self._load_directory(path=path)

        if self._is_zip(path=path):
            return self._load_zip(path=path)

        if self.is_file(path=path):
            return self._load_file(path=path)

        raise ValueError(f"Unable to load path: {path}")

    def _load_file(
            self,
            path: pathlib.Path | str,
    ) -> list[Document]:

        path = pathlib.Path(path)
        extension = path.suffix.lower()

        loader_cls = self._loaders.get(extension)

        if loader_cls is None:
            raise ValueError(
                f"Unsupported file extension: {extension}"
            )

        return loader_cls().load(path=path)

    def _load_directory(
            self,
            path: pathlib.Path | str,
            *,
            show_progress: bool = True,
    ) -> list[Document]:

        path = pathlib.Path(path)
        documents: list[Document] = []

        # Only collect supported files.
        files = [
            child
            for child in path.rglob("*")
            if child.is_file()
               and (
                       child.suffix.lower() in self._loaders
                       or child.suffix.lower() == ".zip"
               )
        ]

        progress = tqdm(
            files,
            desc="Loading documents",
            unit="file",
            dynamic_ncols=True,
            disable=not show_progress,
            leave=show_progress,
        )

        for file_path in progress:

            progress.set_postfix_str(
                file_path.name,
                refresh=False,
            )

            try:

                if file_path.suffix.lower() == ".zip":
                    documents.extend(
                        self._load_zip(
                            path=file_path,
                            show_progress=False,
                        )
                    )

                else:
                    documents.extend(
                        self._load_file(path=file_path)
                    )

            except ValueError:
                continue

        return documents

    def _load_zip(
            self,
            path: pathlib.Path | str,
            *,
            show_progress: bool = True,
    ) -> list[Document]:

        path = pathlib.Path(path)
        documents: list[Document] = []

        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = pathlib.Path(tmp)

            with zipfile.ZipFile(path, "r") as zf:
                members = zf.infolist()

                with tqdm(
                        total=len(members),
                        desc=f"Extracting {path.name}",
                        unit="file",
                        dynamic_ncols=True,
                        disable=not show_progress,
                        leave=show_progress,
                ) as progress:
                    for member in members:
                        zf.extract(member, tmp_path)

                        progress.update(1)
                        progress.set_postfix_str(
                            pathlib.Path(member.filename).name,
                            refresh=False,
                        )

            documents.extend(
                self._load_directory(
                    tmp_path,
                    show_progress=show_progress,
                )
            )

        return documents
