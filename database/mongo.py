from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URI

mongo_client = AsyncIOMotorClient(MONGO_URI)

db = mongo_client["savihub"]

files_collection = db["files"]
users_collection = db["users"]
async def add_file(title, quality, size, file_id):

    await files_collection.insert_one(
        {
            "title": title.lower(),
            "quality": quality,
            "size": size,
            "file_id": file_id
        }
    )


async def get_files(title):

    return await files_collection.find(
        {
            "title": title.lower()
        }
    ).to_list(length=50)
