# create collections
from db.qdrant import QdrantDB
from services.logger import Logger
from services.utils import get_collection_list


async def create_collections():
    try:
        for collection in (await get_collection_list()):
            await QdrantDB.create_collection(collection)
        return None

    except Exception as e:
        await Logger.error_log(__name__,'create_collections',e)
        return None


async def delete_collections():
    try:
        for collection in (await get_collection_list()):
            await QdrantDB.delete_collection(collection)
        return None

    except Exception as e:
        await Logger.error_log(__name__,'delete_collections',str(e))
        return None