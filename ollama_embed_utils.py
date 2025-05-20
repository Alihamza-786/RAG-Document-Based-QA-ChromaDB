import requests
from chromadb.utils.embedding_functions import EmbeddingFunction
from typing import List, Union

class OllamaEmbeddingFunction(EmbeddingFunction):
    def __init__(
        self,
        model_name: str = "mxbai-embed-large",
        endpoint: str = "http://localhost:11434/api/embeddings",
        timeout: int = 30
    ):
        self.model_name = model_name
        self.endpoint = endpoint
        self.timeout = timeout

    def embed_documents(self, documents: List[str]) -> List[List[float]]:
        return self._get_embeddings(documents)

    def embed_query(self, query: str) -> List[float]:
        return self._get_embeddings([query])[0]

    def __call__(self, input: Union[str, List[str]]) -> List[List[float]]:
        if isinstance(input, str):
            return [self.embed_query(input)]
        return self.embed_documents(input)

    def _get_embeddings(self, texts: List[str]) -> List[List[float]]:
        embeddings = []
        for text in texts:
            try:
                response = requests.post(
                    self.endpoint,
                    json={"model": self.model_name, "prompt": text},
                    timeout=self.timeout
                )
                response.raise_for_status()
                data = response.json()
                embeddings.append(data["embedding"])
            except Exception as e:
                print(f"Failed to get embedding for: {text[:50]}... Error: {e}")
                embeddings.append([0.0] * 1024)  # Fallback dummy vector
        return embeddings