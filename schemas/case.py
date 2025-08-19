from pydantic import BaseModel
from typing import Optional, List

class CaseBase(BaseModel):
    title: str
    description: str
    detectives: Optional[List[str]] = []
    related_cases: Optional[List[str]] = []
    victim_ids: Optional[List[str]] = []

class CaseCreate(CaseBase):
    pass

class CaseUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    detectives: Optional[List[str]] = []
    related_cases: Optional[List[str]] = []
    victim_ids: Optional[List[str]] = []

class CaseDB(CaseBase):
    id: str

    class Config:
        orm_mode = True
