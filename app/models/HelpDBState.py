from pydantic import BaseModel

class HelpDBState(BaseModel):
    isDBPresent: False
    size: 0
    lastUpdated: str | None = None