from database import case_collection
from bson import ObjectId

def case_helper(case) -> dict:
    return {
        "id": str(case["_id"]),
        "title": case["title"],
        "description": case["description"],
        "detectives": case.get("detectives", []),
        "related_cases": case.get("related_cases", []),
        "victim_ids": case.get("victim_ids", [])
    }

async def retrieve_cases():
    cases = []
    async for case in case_collection.find():
        cases.append(case_helper(case))
    return cases

async def retrieve_case(id: str):
    case = await case_collection.find_one({"_id": ObjectId(id)})
    return case_helper(case) if case else None

async def add_case(case_data: dict) -> dict:
    case = await case_collection.insert_one(case_data)
    new_case = await case_collection.find_one({"_id": case.inserted_id})
    return case_helper(new_case)

async def update_case(id: str, data: dict):
    if len(data) < 1:
        return False
    case = await case_collection.find_one({"_id": ObjectId(id)})
    if case:
        await case_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        return True
    return False

async def delete_case(id: str):
    case = await case_collection.find_one({"_id": ObjectId(id)})
    if case:
        await case_collection.delete_one({"_id": ObjectId(id)})
        return True
    return False
