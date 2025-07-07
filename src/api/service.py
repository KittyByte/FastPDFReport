from typing import Literal
from fastapi import APIRouter


router = APIRouter(tags=['Service'])

@router.get('/setup')
async def setup_database() -> Literal['OK']:
    
    return 'OK'

