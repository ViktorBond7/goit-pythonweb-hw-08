

from requests import Session
from src.models.contact import Contact
from src.repositories import contact_repo
from fastapi import HTTPException, status

def get_all_contacts(session: Session) -> list[Contact]:
    return contact_repo.get_all_contacts(session)

def create_contact(session: Session, contact: Contact) -> Contact:
    db_contact = contact_repo.get_contact_by_email(session, contact.email)
    if db_contact:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Contact with email {contact.email} already exists.")
    return contact_repo.create_contact(session, contact)

def get_contact_by_id(session: Session, contact_id: int) -> Contact | None:
    return contact_repo.get_contact_by_id(session, contact_id)