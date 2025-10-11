from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from app.pdf_reports.routers import router as pdf_router
from app.services.routers import router as service_router
from app.users.routers import router as user_router



app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(pdf_router)
app.include_router(user_router)
app.include_router(service_router)

origins = [
    "http://localhost",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
