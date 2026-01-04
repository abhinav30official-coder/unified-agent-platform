from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Unified Agent Platform")

app.include_router(router)
