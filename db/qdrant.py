import os

import numpy as np
from qdrant_client import AsyncQdrantClient
from qdrant_client.http.models import VectorParams, Distance
from qdrant_client import models
from dotenv import load_dotenv

load_dotenv()


class QdrantDB:
    _client = None

    @classmethod
    async def make_connection(cls):
        if cls._client is None:
            cls._client = AsyncQdrantClient(url=os.getenv("QDRANT_URI"),port=6333)

        return cls._client

    @staticmethod
    async def create_collection(collection:str):
        if not await QdrantDB._client.collection_exists(collection):
            await QdrantDB._client.create_collection(
                collection_name=collection,
                vectors_config=VectorParams(
                    size=786,
                    distance=Distance.COSINE
                )
            )


    @staticmethod
    async def insert_vectors(collection_name:str,embeddings:np.array,payload:str):
        points = [
            models.PointStruct(
                id = i+1,
                vector=vector,
                payload={
                    'section' : 'fitness'
                }
            )
            for i, vector in enumerate(embeddings)
        ]
        await QdrantDB._client.upsert(
            collection_name=collection_name,
            points=points
        )


    @staticmethod
    async def query_points(collection_name:str,query:np.array):
        result = QdrantDB._client.query_ponints(
            collection_name=collection_name,
            query=query
        )
        return result

    @staticmethod
    async def close_connection() -> None:
        if QdrantDB._client is not None:
            await QdrantDB._client.close()
            return None
        return None





