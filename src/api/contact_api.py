from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.schemas.contact import ContactResponse, ContactRequest
from src.db.sesion import open_session
from src.services import contact_service


router = APIRouter()


# Get all contacts from db
@router.get("/contacts/", response_model=list[ContactResponse])
def get_all_contacts(session: Session = Depends(open_session)):
    contacts = contact_service.get_all_contacts(session)
    return [ContactResponse.model_validate(c) for c in contacts]

# Create new contact
@router.post("/contacts/", response_model=ContactResponse)
def create_contact(contact: ContactRequest, session: Session = Depends(open_session)):
    new_contact = contact_service.create_contact(session, contact)
    return ContactResponse.model_validate(new_contact)

# Get contact by id
@router.get("/contacts/{contact_id}", response_model=ContactResponse)
def get_contact_by_id(contact_id: int, session: Session = Depends(open_session)):
    contact = contact_service.get_contact_by_id(session, contact_id)
    if not contact:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
    return ContactResponse.model_validate(contact)