from fastapi import FastAPI
from app.routes import code_routes

app = FastAPI(
    title="Code Explainer API",
    description="API para explicar trechos de código e sugerir melhorias usando OpenAI",
    version="0.1.0"
)

app.include_router(code_routes.router)