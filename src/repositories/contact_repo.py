
from sqlalchemy.orm import Session

from src.models.contact import Contact


def get_all_contacts(session: Session) -> list[Contact]:
    return session.query(Contact).all()

def create_contact(session: Session, contact: Contact) -> Contact:
    new_contact = Contact(**contact.model_dump())
    session.add(new_contact)
    session.commit()
    session.refresh(new_contact)
    print(f"Created contact: {new_contact}")
    return new_contact

def get_contact_by_id(session: Session, contact_id: int) -> Contact | None:
    return session.query(Contact).filter(Contact.id == contact_id).first()

def get_contact_by_email(session: Session, email: str) -> Contact | None:
    return session.query(Contact).filter(Contact.email == email).first()