from .embedding_chunker.embedding import ChunkingEmbedder
from langchain_experimental.text_splitter import SemanticChunker
from langchain_core.documents import Document

class SemanticChuker:
    def __init__(self):
        self.chunking_embedder = ChunkingEmbedder()
        self.semantic_chunker = SemanticChunker(
            embeddings=self.chunking_embedder.model,
            breakpoint_threshold_amount=90,
            breakpoint_threshold_type="percentile",
            min_chunk_size=400
        )

    def split_document(self, document: list[Document])-> list[Document]:
        return self.semantic_chunker.split_documents(document)
