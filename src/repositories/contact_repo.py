from sqlalchemy.orm import Session

from src.models.contact import Contact


def get_all_contacts(
    session: Session,
    first_name: str | None = None,
    last_name: str | None = None,
    email: str | None = None,
) -> list[Contact]:
    query = session.query(Contact)

    if first_name:
        query = query.filter(Contact.first_name.ilike(f"%{first_name}%"))
    if last_name:
        query = query.filter(Contact.last_name.ilike(f"%{last_name}%"))
    if email:
        query = query.filter(Contact.email.ilike(f"%{email}%"))

    return query.all()


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


def update_contact(session: Session, db_contact: Contact) -> Contact:
    session.add(db_contact)
    session.commit()
    session.refresh(db_contact)
    return db_contact


def delete_contact(session: Session, db_contact: Contact) -> None:
    session.delete(db_contact)
    session.commit()
