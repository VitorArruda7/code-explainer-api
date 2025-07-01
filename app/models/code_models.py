from pydantic import BaseModel

class CodeRequest(BaseModel):
    code_snippet: str
    language: str

class CodeResponse(BaseModel):
    explanation: str
    improvements: str