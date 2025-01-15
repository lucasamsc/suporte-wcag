from search import search_rule
from llm import ask_llm, generate_prompt

if __name__ == "__main__":
    # Entrada do usuário
    query = input("Pergunte sobre WCAG: ")

    # Buscar regra mais relevante
    results = search_rule(query)

    # Exibir os resultados e perguntar ao LLM
    for result in results:
        print("\nRegra Encontrada:")
        print(f"ID: {result[0]}")
        print(f"Título: {result[1]}")
        print(f"Descrição: {result[2]}")

        # Gerar o prompt e enviar para o LLM
        prompt = generate_prompt(result)
        answer = ask_llm("llama3.2:3b", prompt)

        # Exibir a resposta do LLM
        print("\nResposta do LLM:")
        print(answer)
