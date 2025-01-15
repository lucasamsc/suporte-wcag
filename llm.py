import ollama

# Função para enviar perguntas ao LLM
def ask_llm(model, prompt):
    response_text = ""
    for result in ollama.generate(model=model, prompt=prompt):
        if isinstance(result, dict) and 'response' in result:
            response_text += result['response']
    if not response_text:
        return "Desculpe, não consegui gerar uma resposta."
    return response_text.strip()

# Função para criar um prompt com base na regra encontrada
def generate_prompt(rule):
    return f"""
Você é um especialista em acessibilidade digital. Aqui está uma regra da WCAG que você deve explicar:

ID: {rule[0]}
Título: {rule[1]}
Descrição: {rule[2]}

Explique essa regra de maneira simples e dê exemplos práticos.
"""

if __name__ == "__main__":
    # Teste do LLM
    example_rule = ("1", "Conteúdo Não Textual", "Forneça uma descrição em texto para todo conteúdo não textual.")
    prompt = generate_prompt(example_rule)
    resposta = ask_llm("llama3.2:3b", prompt)
    print("Resposta do LLM:", resposta)