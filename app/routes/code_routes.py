from fastapi import APIRouter
from app.models.code_models import CodeRequest, CodeResponse
from app.services.code_service import OpenAIService

router = APIRouter()
openai_service = OpenAIService()

@router.get("/health")
async def health_check():
    return {"status": "ok"}

@router.post("/explain", response_model=CodeResponse)
async def explain_code(request: CodeRequest):
    result = openai_service.explain_code(request.code_snippet, request.language)
    return CodeResponse(
        explanation=result["explanation"],
        improvements=result["improvements"]
    )