import faiss
import numpy as np
import os

class VectorStore:
    _instance = None

    def __new__(cls, dimension=768):
        if cls._instance is None:
            cls._instance = super(VectorStore, cls).__new__(cls)
            cls._instance.dimension = dimension
            cls._instance.index = faiss.IndexFlatL2(dimension)
            cls._instance.data = []
        return cls._instance

    def store(self, embedding, metadata):
        vector = np.array([embedding]).astype("float32")
        self.index.add(vector)
        self.data.append(metadata)

    def search(self, embedding, k=3):
        if self.index.ntotal == 0:
            return []

        vector = np.array([embedding]).astype("float32")
        distances, indices = self.index.search(vector, k)

        results = []
        for i in indices[0]:
            if i < len(self.data):
                results.append(self.data[i])

        return results
    def save(self, path="faiss.index"):
        faiss.write_index(self.index, path)
        np.save("metadata.npy", self.data)

    def load(self, path="faiss.index"):
        if os.path.exists(path):
            self.index = faiss.read_index(path)
            self.data = list(np.load("metadata.npy", allow_pickle=True))
