from pathlib import Path
from langchain_core.documents import Document
from langchain_community.document_loaders import TextLoader
from .base import BaseLoader


class TxtLoader(BaseLoader):
    """Loader for plain text (``.txt``) files.

    Wraps :class:`TextLoader` to read a text file from disk and return its
    contents as a list of :class:`Document` objects. The file's encoding is
    detected automatically.
    """

    def load(self, path: Path | str) -> list[Document]:
        """Load a plain text file and return its contents as documents.

        Parameters
        ----------
        path : pathlib.Path or str
            Path to the text file to load. Strings are coerced to
            :class:`pathlib.Path` before use.

        Returns
        -------
        list of Document
            Documents parsed from the text file. ``TextLoader`` typically
            returns a single :class:`Document` containing the full file
            contents.

        Raises
        ------
        FileNotFoundError
            If no file exists at ``path``.
        RuntimeError
            If the file's encoding cannot be detected or decoded.

        Notes
        -----
        Encoding is detected automatically via ``autodetect_encoding=True``,
        so callers do not need to specify an encoding explicitly.

        Examples
        --------
        >>> loader_cls = TxtLoader()
        >>> docs = loader_cls.load("notes.txt")
        >>> docs[0].page_content[:20]
        'Meeting notes for th'
        """
        path = Path(path)
        loader = TextLoader(
            file_path=path,
            autodetect_encoding=True
        )
        return loader.load()
