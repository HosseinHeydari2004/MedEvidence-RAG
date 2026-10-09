from langchain_huggingface.embeddings import HuggingFaceEmbeddings


class ChunkingEmbedder:
    def __init__(self, embedding_model_name: str = "BAAI/bge-small-en-v1.5"):
        self.model = HuggingFaceEmbeddings(
            model_name=embedding_model_name,
            encode_kwargs={
                "normalize_embeddings": True
            },
        )


