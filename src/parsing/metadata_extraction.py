from ..schemas.metadata import DocumentMetadata
from langchain_core.documents import Document
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()


class MetadataExtractor:

    def __init__(self) -> None:
        self.chat_model = init_chat_model(
            "auto",
            model_provider="openrouter"
        )
        self._structured_llm = self.chat_model.with_structured_output(DocumentMetadata)

    def extract_metadata(self, document: list[Document]) -> DocumentMetadata:
        full_text = "\n".join(
            docs.page_content
            for docs in document[:6]
        )
        return self._structured_llm.invoke(
            f"""
            Extract metadata from the following document.
            Return:
            - title
            - author
            - year
            - document_type
            - language
            
            Document:
            
            {full_text[:6000]}
            """
        )
