from pydantic import BaseModel, ConfigDict
from datetime import date

class ContactRequest(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone_number: str
    birthday: date
    additional_data: str | None = None



class ContactResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    first_name: str
    last_name: str
    email: str
    phone_number: str
    birthday: date
    additional_data: str | None = None

    # class Config:
    #     orm_mode = True
