class MockOpenAIService:
    def explain_code(self, code_snippet: str, language: str) -> str:
        return f"Mock explanation for {language} code: {code_snippet}"