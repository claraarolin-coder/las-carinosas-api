from fastapi import APIRouter, HTTPException
from models.case import (
    retrieve_cases,
    retrieve_case,
    add_case,
    update_case,
    delete_case
)
from schemas.case import CaseCreate, CaseUpdate, CaseDB

router = APIRouter()

@router.get("/", response_model=list[CaseDB])
async def get_cases():
    return await retrieve_cases()

@router.get("/{id}", response_model=CaseDB)
async def get_case(id: str):
    case = await retrieve_case(id)
    if case:
        return case
    raise HTTPException(status_code=404, detail="Case not found")

@router.post("/", response_model=CaseDB)
async def create_case(case: CaseCreate):
    return await add_case(case.dict())

@router.patch("/{id}")
async def update_case_data(id: str, case: CaseUpdate):
    updated = await update_case(id, case.dict(exclude_unset=True))
    if updated:
        return {"message": "Case updated successfully"}
    raise HTTPException(status_code=404, detail="Case not found")

@router.delete("/{id}")
async def delete_case_data(id: str):
    deleted = await delete_case(id)
    if deleted:
        return {"message": "Case deleted successfully"}
    raise HTTPException(status_code=404, detail="Case not found")
