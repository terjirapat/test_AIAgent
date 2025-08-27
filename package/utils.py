from pydantic import BaseModel
from typing import Optional

class Prompt(BaseModel):
    model_name: str
    system_prompt: str
    temperature: Optional[float] = 0