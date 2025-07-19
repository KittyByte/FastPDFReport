from fastapi import FastAPI
from src.pdf_reports.routers import router as pdf_router
from src.services.routers import router as service_router



app = FastAPI()
app.include_router(pdf_router)
app.include_router(service_router)


