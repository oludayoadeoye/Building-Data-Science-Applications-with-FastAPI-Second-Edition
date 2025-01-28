from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

uri = "mongodb://admin:admin@localhost:27017/?authSource=admin"
client = AsyncIOMotorClient(uri)
database = client["chapter06_mongo"]


def get_database() -> AsyncIOMotorDatabase:
    return database
