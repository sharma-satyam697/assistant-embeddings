import torch
from sentence_transformers import SentenceTransformer

from services.logger import Logger


class EmbeddingModel:
    _model = None

    @classmethod
    async def _initialize_model(cls):
        """
        Initializes the Sentence Transformer model if it has not been initialized yet.
        """
        try:
            if cls._model is None:
                cls._model = SentenceTransformer("all-mpnet-base-v2")
        except Exception as e:
            await Logger.error_log(file_name=__name__, func_name="_initialize_model", error=e)

    @staticmethod
    async def encode_sentences(list_of_sentences: list) -> torch.Tensor | None:
        try:
            await EmbeddingModel._initialize_model()
            embeddings = EmbeddingModel._model.encode(list_of_sentences, show_progress_bar=True, convert_to_tensor=True)
            return embeddings
        except Exception as e:
            await Logger.error_log(file_name=__name__, func_name="encode_sentences", error=e)
            return None