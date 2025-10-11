import requests
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

class RetrieverAgent:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
        self.contexts = []
        self.embeddings = None
        self.index = None

    def load_data():
        data = requests.get(url).json()

        self.contexts = []
        for sample in data[:limit]:
            joined_text = " ".join([c[1] for c in sample["context"]])
            self.contexts.append(joined_text)
        print(f" Đã lấy {len(self.contexts)} đoạn context đầu tiên.")

    def build_index(self):
        print(" Đang tạo embedding vectors ...")
        self.embeddings = self.model.encode(self.contexts, convert_to_numpy=True, show_progress_bar=True)

        d = self.embeddings.shape[1]
        self.index = faiss.IndexFlatL2(d)
        self.index.add(self.embeddings)
        print(" FAISS index đã sẵn sàng, chứa", self.index.ntotal, "vector.")

    def search(self, query, k=5):
        if self.index is None:
            raise ValueError("Index chưa được xây dựng. Hãy gọi build_index() trước.")
        
        query_vec = self.model.encode([query], convert_to_numpy=True)
        distances, indices = self.index.search(query_vec, k)

        results = []
        for i, idx in enumerate(indices[0]):
            results.append({
                "rank": i + 1,
                "distance": float(distances[0][i]),
                "context": self.contexts[idx][:500] + "..."
            })
        return results