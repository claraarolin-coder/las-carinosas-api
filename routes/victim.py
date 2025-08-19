from fastapi import APIRouter, HTTPException
from models.victim import (
    retrieve_victims,
    retrieve_victim,
    add_victim,
    update_victim,
    delete_victim
)
from schemas.victim import VictimCreate, VictimUpdate, VictimDB

router = APIRouter()

@router.get("/", response_model=list[VictimDB])
async def get_victims():
    return await retrieve_victims()

@router.get("/{id}", response_model=VictimDB)
async def get_victim(id: str):
    victim = await retrieve_victim(id)
    if victim:
        return victim
    raise HTTPException(status_code=404, detail="Victim not found")

@router.post("/", response_model=VictimDB)
async def create_victim(victim: VictimCreate):
    return await add_victim(victim.dict())

@router.patch("/{id}")
async def update_victim_data(id: str, victim: VictimUpdate):
    updated = await update_victim(id, victim.dict(exclude_unset=True))
    if updated:
        return {"message": "Victim updated successfully"}
    raise HTTPException(status_code=404, detail="Victim not found")

@router.delete("/{id}")
async def delete_victim_data(id: str):
    deleted = await delete_victim(id)
    if deleted:
        return {"message": "Victim deleted successfully"}
    raise HTTPException(status_code=404, detail="Victim not found")
