from pydantic import BaseModel

class Query(BaseModel):
    user_question: str
    system_role: str