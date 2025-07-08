from fastapi import FastAPI
from src.api import pdf_router, service_router



app = FastAPI()
app.include_router(pdf_router)
app.include_router(service_router)



