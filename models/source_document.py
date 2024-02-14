from pydantic import BaseModel

class SourceDocument(BaseModel):
    title: str
    source: str