from fastapi import APIRouter, Depends
from app.models.code_models import CodeRequest, CodeResponse
from app.services.mock_openai_service import MockOpenAIService
from app.services.code_service import OpenAIService

router = APIRouter()
openai_service = OpenAIService()

def get_openai_service():
    return OpenAIService()

@router.get("/health")
async def health_check():
    return {"status": "ok"}

@router.post("/explain")
async def explain_code(request: CodeRequest, openai_service = Depends(get_openai_service)):
    explanation = openai_service.explain_code(request.code_snippet, request.language)
    return {"explanation": explanation}