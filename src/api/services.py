from typing import Literal
from fastapi import APIRouter
from src.orm.models.base_model import Base
from src.database import engine


router = APIRouter(tags=['Service'])


@router.get('/setup')
async def setup_database() -> Literal['OK']:
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    return 'OK'

