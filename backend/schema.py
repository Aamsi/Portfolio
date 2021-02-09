from pydantic import BaseModel
from typing import List, Optional

class PydanticCategory(BaseModel):
    name: str

    class Config:
        orm_mode = True


class PydanticProject(BaseModel):
    title: str
    description: str
    picture: Optional[str]
    url: str
    categories: List[PydanticCategory]

    class Config:
        orm_mode = True
