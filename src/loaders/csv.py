from .base import BaseLoader
from pathlib import Path
from langchain_core.documents import Document
from langchain_community.document_loaders import CSVLoader


class CsvLoader(BaseLoader):
    """
    Load and parse CSV files into a list of `Document` objects.

    `CsvLoader` is a thin wrapper around
    `langchain_community.document_loaders.CSVLoader` that provides a
    simplified `load` interface. It accepts either a `pathlib.Path` or a
    string path, automatically detects the file encoding, and returns one
    `Document` per CSV row.

    Parameters
    ----------
    Inherited from `BaseLoader`. This class does not define its own
    `__init__` parameters.

    Attributes
    ----------
    Inherited from `BaseLoader`.

    Methods
    -------
    load(path)
        Load the CSV file at `path` and return its rows as `Document`
        objects.

    See Also
    --------
    langchain_community.document_loaders.CSVLoader : The underlying
        loader used to parse the CSV file.
    langchain_core.document_loaders.BaseLoader : The base class this
        loader inherits from.

    Notes
    -----
    Encoding is detected automatically via the `autodetect_encoding`
    flag passed to the underlying `CSVLoader`. Each returned `Document`
    typically includes metadata such as the source file path and the
    row index.

    Examples
    --------
    Load a CSV file using a string path:

    >>> loader = CsvLoader()
    >>> docs = loader.load("data/records.csv")
    >>> len(docs)
    42

    Load a CSV file using a `pathlib.Path`:

    >>> from pathlib import Path
    >>> loader = CsvLoader()
    >>> docs = loader.load(Path("data/records.csv"))
    >>> docs[0].metadata["source"]
    'data/records.csv'
    """

    def load(self, path: Path | str) -> list[Document]:
        """
        Load documents from a CSV file.

        Parameters
        ----------
        path : pathlib.Path or str
            Path to the CSV file to be loaded.

        Returns
        -------
        list of Document
            One `Document` per row in the CSV file.
        """
        path = Path(path)
        loader = CSVLoader(
            file_path=path,
            autodetect_encoding=True
        )
        docs = loader.load()
        return docs
