from pydantic import BaseModel

class HelpDBState(BaseModel):
    isDBPresent: bool
    size: int
    lastUpdated: str