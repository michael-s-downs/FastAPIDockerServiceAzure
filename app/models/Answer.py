from pydantic import BaseModel
from typing import List
from SourceDocument import SourceDocument  

class Answer(BaseModel):
    user_question: str
    system_role: str
    response: str
    source_documents: List[SourceDocument]