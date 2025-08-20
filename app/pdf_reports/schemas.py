from datetime import date

from pydantic import BaseModel


class CreatePDFSchema(BaseModel):
    chat_id: int
    date_from: date
    date_to: date

