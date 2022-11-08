from typing import List

from src.context.user.domain.abstract_user_repository import IUserRepository
from src.context.user.domain.user import User
from src.context.shared.persistence.sqlalchemy.config import SessionLocal
from src.context.user.infrastructure.sqlalchemy.user_entity import start_mapper

start_mapper()


class SqlAlchemyUserRepository(IUserRepository):

    def save(self, user: User):
        session = SessionLocal()
        session.add(user)
        session.commit()
        session.refresh(user)
        session.close()

    def list_all(self) -> List[User]:
        return SessionLocal().query(User).all()
