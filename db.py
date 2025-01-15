import faiss
import pickle

class VectorDatabase:
    def __init__(self, index_path, embeddings_path):
        self.index_path = index_path
        self.embeddings_path = embeddings_path

    def save_index(self, embeddings):
        d = embeddings.shape[1]
        index = faiss.IndexFlatL2(d)
        index.add(embeddings)
        faiss.write_index(index, self.index_path)

    def load_index(self):
        return faiss.read_index(self.index_path)

    def save_embeddings(self, embeddings):
        with open(self.embeddings_path, 'wb') as f:
            pickle.dump(embeddings, f)

    def load_embeddings(self):
        with open(self.embeddings_path, 'rb') as f:
            return pickle.load(f)
