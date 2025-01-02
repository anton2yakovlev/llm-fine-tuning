from fastapi import FastAPI

from .api import health_router, llama_router


app = FastAPI()

app.include_router(health_router)
app.include_router(llama_router)
