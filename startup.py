# create collections
from db.qdrant import QdrantDB
from services.utils import get_collection_list


async def create_collections():
    for collection in (await get_collection_list()):
        await QdrantDB.create_collection(collection)
    return None