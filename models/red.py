from typing import Optional
from pydantic import BaseModel

class Parrafo(BaseModel):
    texto1: str
    texto2: list[str]

class Red(BaseModel):
    id:Optional[str]
    parrafo: Parrafo