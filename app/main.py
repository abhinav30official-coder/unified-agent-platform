from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.api.routes import router

app = FastAPI(title="Unified Agent Platform")

@app.get("/")
def root():
    return RedirectResponse(url="/docs")

app.include_router(router)
