from datetime import date, datetime
from typing import List, Optional
from pydantic import BaseModel, EmailStr, Field


class ContactSchema(BaseModel):
    first_name: str = Field(max_length=150)
    last_name: str = Field(max_length=150)
    email: EmailStr
    phone_number: str = Field(max_length=30)
    birthday : date
    add_info: Optional[str]=''


class ContactResponseSchema(ContactSchema):
    id: int = 1
    created_at: datetime

    class Config:
        from_attributes = True