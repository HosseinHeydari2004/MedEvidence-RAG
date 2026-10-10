from langchain_core.documents import Document

from .cleaner.pipeline import CleanerPipeline
from .chunking.semantic import SemanticChuker
from .parsing.metadata_extraction import MetadataExtractor


class PreprocessingPipeline:
    def __init__(self):
        self._cleaner = CleanerPipeline()
        self._semantic_chuker = SemanticChuker()
        self._metadata_extractor = MetadataExtractor()

    def process(self, document: list[Document]) -> list[Document]:
        cleaned_docs: list[Document] = []

        for doc in document:
            cleaned_text = self._cleaner.clean(
                text=doc.page_content
            )

            cleaned_doc = Document(
                page_content=cleaned_text,
                metadata=doc.metadata.copy()
            )
            cleaned_docs.append(cleaned_doc)

        extracted_metadata = (
            self._metadata_extractor.extract_metadata(
                document=cleaned_docs
            )
        )

        processed_docs: list[Document] = []

        for doc in cleaned_docs:
            merged_metadata = {
                **doc.metadata,
                **extracted_metadata.model_dump(exclude_none=True)
            }

            processed_docs.append(
                Document(
                    page_content=doc.page_content,
                    metadata=merged_metadata
                )
            )

        return self._semantic_chuker.split_document(
            document=processed_docs
        )
