from pydantic import BaseModel
from datetime import date


class CreatePDFSchema(BaseModel):
    chat_id: int
    date_from: date
    date_to: date

