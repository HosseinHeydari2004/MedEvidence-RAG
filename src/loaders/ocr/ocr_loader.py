from pytesseract import image_to_string

from ..base import BaseLoader
from langchain_core.documents import Document
from pathlib import Path
from pdf2image import convert_from_path


class OcrLoader(BaseLoader):

    def load(self, path: Path | str, lang: str = "eng", dpi: int = 300) -> list[Document]:
        pdf_path = Path(path)
        pages = convert_from_path(pdf_path, dpi=dpi)
        docs = []
        for page_number, page_image in enumerate(pages, start=1):
            text = image_to_string(page_image, lang=lang)
            text = text.strip()
            if not text:
                continue
            document = Document(
                page_content=text,
                metadata={
                    "source": str(pdf_path),
                    "filename": pdf_path.name,
                    "page_number": page_number,

                }
            )
            docs.append(document)
        return docs
