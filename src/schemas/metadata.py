from pydantic import BaseModel, Field

class DocumentMetadata(BaseModel):
    title: str = Field(
        description="The title of the document.",
    )
    author: str = Field(
        default=None,
    )
    year: str = Field(
        default=None,
    )
    document_type: str = Field(
        description="Type of document, e.g. research_paper, book, report, documentation"
    )
    language: str = Field(
        description="Main language of the document",
    )