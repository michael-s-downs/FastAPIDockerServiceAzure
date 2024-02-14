from pydantic import BaseModel

class Answer(BaseModel):
    user_question: str
    system_role: str