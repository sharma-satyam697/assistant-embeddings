import asyncio

from db.qdrant import QdrantDB
from services.logger import Logger
from startup import create_collections, delete_collections


async def main():
    await QdrantDB.make_connection()
    # delete all previous colelcitons
    await delete_collections()
    await Logger.info_log("Connection setup successfully")
    await create_collections()
    # upsert all the data on

    await Logger.info_log("Closing Qdrant connection")
    await QdrantDB.close_connection()



if __name__ == '__main__':
    asyncio.run(main())