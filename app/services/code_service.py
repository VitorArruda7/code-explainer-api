import os
from openai import OpenAI

class OpenAIService:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def explain_code(self, code_snippet: str, language: str) -> dict:
        prompt = f"""
Explique o seguinte trecho de código em {language} de forma didática para um desenvolvedor júnior, linha por linha se possível, e sugira melhorias ou boas práticas ao final:

Código:
{code_snippet}
"""
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é um assistente que explica códigos de maneira clara e sugere melhorias."},
                {"role": "user", "content": prompt}
            ]
        )

        explanation_text = response.choices[0].message.content.strip()

        return {
            "explanation": explanation_text,
            "improvements": "As sugestões de melhoria estão inclusas na explicação acima."
        }