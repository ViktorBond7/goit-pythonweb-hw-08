from sqlalchemy.orm import Session
from src.models.contact import Contact
from src.repositories import contact_repo
from fastapi import HTTPException, status
from src.schemas.contact import ContactRequest, ContactUpdateRequest
from datetime import date, timedelta


def get_all_contacts(
    session: Session,
    first_name: str | None = None,
    last_name: str | None = None,
    email: str | None = None,
) -> list[Contact]:
    return contact_repo.get_all_contacts(session, first_name, last_name, email)


def get_upcoming_birthdays(session: Session, days: int = 7) -> list[Contact]:
    today = date.today()
    end_date = today + timedelta(days=days)
    contacts = contact_repo.get_all_contacts(session)

    upcoming_contacts: list[Contact] = []
    for contact in contacts:
        next_birthday = contact.birthday.replace(year=today.year)
        if next_birthday < today:
            next_birthday = next_birthday.replace(year=today.year + 1)

        if today <= next_birthday <= end_date:
            upcoming_contacts.append(contact)

    return upcoming_contacts


def create_contact(session: Session, contact: ContactRequest) -> Contact:
    db_contact = contact_repo.get_contact_by_email(session, contact.email)
    if db_contact:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Contact with email {contact.email} already exists.",
        )
    return contact_repo.create_contact(session, contact)


def get_contact_by_id(session: Session, contact_id: int) -> Contact | None:
    db_contact = contact_repo.get_contact_by_id(session, contact_id)
    if not db_contact:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found"
        )
    return db_contact


def update_contact(
    session: Session, db_contact: Contact, contact: ContactUpdateRequest
) -> Contact:
    update_data = contact.model_dump(exclude_unset=True)

    if "email" in update_data and update_data["email"] != db_contact.email:
        existing_contact = contact_repo.get_contact_by_email(
            session, update_data["email"]
        )
        if existing_contact and existing_contact.id != db_contact.id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Contact with email {update_data['email']} already exists.",
            )

    for field, value in update_data.items():
        setattr(db_contact, field, value)

    return contact_repo.update_contact(session, db_contact)


def delete_contact(session: Session, db_contact: Contact) -> None:
    db_contact = contact_repo.get_contact_by_id(session, db_contact.id)
    if not db_contact:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found"
        )
    contact_repo.delete_contact(session, db_contact)
