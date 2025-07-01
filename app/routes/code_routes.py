from fastapi import APIRouter
from app.models.code_models import CodeRequest, CodeResponse

router = APIRouter()

@router.get("/health")
async def health_check():
    return {"status": "ok"}

@router.post("/explain", response_model=CodeResponse)
async def explain_code(request: CodeRequest):
    explanation = f"Explicação mock para o código em {request.language}."
    improvements = "Sugestões de melhoria mock."
    return CodeResponse(explanation=explanation, improvements=improvements)