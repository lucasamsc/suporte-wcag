import json
from sentence_transformers import SentenceTransformer
from db import VectorDatabase

# Configuração
MODEL_NAME = 'all-MiniLM-L6-v2'
DB = VectorDatabase('embeddings/faiss_index.bin', 'embeddings/embeddings.pkl')

# Carregar modelo SBERT e índice FAISS
model = SentenceTransformer(MODEL_NAME)
index = DB.load_index()

# Carregar regras da WCAG
with open('data/wcag_rules.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    rules = data["regras"]

# Função de busca de regras no banco vetorial
def search_rule(query, top_k=3):
    query_embedding = model.encode([query])
    distances, indices = index.search(query_embedding, top_k)
    return [(rules[i]['id'], rules[i]['titulo_regra'], rules[i]['descricao_regra']) for i in indices[0]]

if __name__ == "__main__":
    # Teste da busca
    query = input("Pergunte sobre WCAG: ")
    results = search_rule(query)

    for result in results:
        print(f"\nID: {result[0]}")
        print(f"Título: {result[1]}")
        print(f"Descrição: {result[2]}")