from fastapi import FastAPI

from .api.health import router as health_router
from .api.llama import router as llama_router


app = FastAPI()

app.include_router(health_router)
app.include_router(llama_router)
