

from requests import Session
from src.models.contact import Contact
from src.repositories import contact_repo


def get_all_contacts(session: Session) -> list[Contact]:
    return contact_repo.get_all_contacts(session)

def create_contact(session: Session, contact: Contact) -> Contact:
    return contact_repo.create_contact(session, contact)