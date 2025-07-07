from pydantic import BaseModel
from datetime import datetime


class CreatePDFSchema(BaseModel):
    chat_id: int
    date_from: datetime
    date_to: datetime





