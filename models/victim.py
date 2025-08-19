from database import victim_collection
from bson import ObjectId

def victim_helper(victim) -> dict:
    return {
        "id": str(victim["_id"]),
        "name": victim["name"],
        "age": victim["age"],
        "family": victim["family"],
        "murder_method": victim["murder_method"],
        "case_id": victim.get("case_id")
    }

async def retrieve_victims():
    victims = []
    async for victim in victim_collection.find():
        victims.append(victim_helper(victim))
    return victims

async def retrieve_victim(id: str):
    victim = await victim_collection.find_one({"_id": ObjectId(id)})
    return victim_helper(victim) if victim else None

async def add_victim(victim_data: dict) -> dict:
    victim = await victim_collection.insert_one(victim_data)
    new_victim = await victim_collection.find_one({"_id": victim.inserted_id})
    return victim_helper(new_victim)

async def update_victim(id: str, data: dict):
    if len(data) < 1:
        return False
    victim = await victim_collection.find_one({"_id": ObjectId(id)})
    if victim:
        await victim_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        return True
    return False

async def delete_victim(id: str):
    victim = await victim_collection.find_one({"_id": ObjectId(id)})
    if victim:
        await victim_collection.delete_one({"_id": ObjectId(id)})
        return True
    return False
