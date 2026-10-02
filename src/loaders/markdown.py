from pathlib import Path

from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_core.documents import Document

from .base import BaseLoader


class MarkdownLoader(BaseLoader):
    """Loader for Markdown (``.md``) files.

    Wraps :class:`UnstructuredMarkdownLoader` to read a Markdown file from
    disk and return its contents as a list of :class:`Document` objects.
    """

    def load(self, path: Path | str) -> list[Document]:
        """Load a Markdown file and return its contents as documents.

        Parameters
        ----------
        path : pathlib.Path or str
            Path to the Markdown file to load. Strings are coerced to
            :class:`pathlib.Path` before use.

        Returns
        -------
        list of Document
            Documents parsed from the Markdown file, one per logical
            section as produced by ``UnstructuredMarkdownLoader``.

        Raises
        ------
        FileNotFoundError
            If no file exists at ``path``.

        Examples
        --------
        >>> loader_cls = MarkdownLoader()
        >>> docs = loader_cls.load("README.md")
        >>> docs[0].page_content[:20]
        '# Project Title\\n\\nThi'
        """
        path = Path(path)
        loader = UnstructuredMarkdownLoader(
            file_path=path
        )
        return loader.load()
