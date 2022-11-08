from sqlalchemy import Column, String, Integer, Table
from sqlalchemy.orm import registry, mapper

from src.context.shared.persistence.sqlalchemy.config import metadata
from src.context.user.domain.user import User

mapper_registry = registry()

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(50)),
    Column("password", String(255)),
    Column("name", String(50)),
    Column("last_name", String(50)),
    Column("email", String(100))
)


def start_mapper():
    mapper(User, users)


# start_mapper()
