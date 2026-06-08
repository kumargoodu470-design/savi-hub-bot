from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URI

mongo_client = AsyncIOMotorClient(MONGO_URI)

db = mongo_client["savihub"]

files_collection = db["files"]
users_collection = db["users"]
