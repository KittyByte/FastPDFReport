from fastapi import FastAPI

from app.pdf_reports.routers import router as pdf_router
from app.services.routers import router as service_router
from app.users.routers import router as user_router

app = FastAPI()

app.include_router(pdf_router)
app.include_router(user_router)
app.include_router(service_router)


