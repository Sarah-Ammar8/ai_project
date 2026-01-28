from fastapi import FastAPI
from .config import APP_NAME
from .routes import router

app = FastAPI(title=APP_NAME)
app.include_router(router)
