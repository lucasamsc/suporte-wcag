import json
from sentence_transformers import SentenceTransformer
from db import VectorDatabase

# Configuração
MODEL_NAME = 'all-MiniLM-L6-v2'
DB = VectorDatabase('embeddings/faiss_index.bin', 'embeddings/embeddings.pkl')

# Carregar modelo SBERT
model = SentenceTransformer(MODEL_NAME)

def generate_embeddings(json_path):
    # Abrir e carregar o arquivo JSON
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Acessar a lista de regras dentro da chave "regras"
    rules = data["regras"]

    # Criar embeddings para as descrições das regras
    descriptions = [rule['descricao_regra'] for rule in rules]
    embeddings = model.encode(descriptions)

    # Salvar embeddings e índice no banco de dados vetorial
    DB.save_embeddings(embeddings)
    DB.save_index(embeddings)
    print("Embeddings gerados e salvos com sucesso!")

if __name__ == "__main__":
    generate_embeddings('data/wcag_rules.json')