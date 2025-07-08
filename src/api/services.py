from typing import Literal
from fastapi import APIRouter
from src.database import drop_and_create_database


router = APIRouter(tags=['Service'])


@router.get('/setup')
async def setup_database() -> Literal['OK']:
    drop_and_create_database()
    return 'OK'

