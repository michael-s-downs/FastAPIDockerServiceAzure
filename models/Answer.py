from pydantic import BaseModel
from typing import List
from models.source_document import SourceDocument  

class Answer(BaseModel):
    user_question: str
    system_role: str
    response: str
    source_documents: List[SourceDocument]