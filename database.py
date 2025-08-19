from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = "mongodb+srv://admin:admin123@crime-cluster.rt1qj37.mongodb.net/?retryWrites=true&w=majority&appName=crime-cluster"

client = AsyncIOMotorClient(MONGO_URL)
database = client["las_carinosas_db"]

victim_collection = database["victims"]
case_collection = database["cases"]
