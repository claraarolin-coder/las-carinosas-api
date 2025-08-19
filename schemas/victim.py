from pydantic import BaseModel
from typing import Optional

class VictimBase(BaseModel):
    name: str
    age: int
    family: str
    murder_method: str
    case_id: Optional[str] = None

class VictimCreate(VictimBase):
    pass

class VictimUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    family: Optional[str] = None
    murder_method: Optional[str] = None
    case_id: Optional[str] = None

class VictimDB(VictimBase):
    id: str

    class Config:
        orm_mode = True
