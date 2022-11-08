from dependency_injector import containers, providers

from src.context.user.infrastructure.sqlalchemy_user_repository import SqlAlchemyUserRepository
from src.context.user.application.create.user_creator import UserCreator
from src.context.user.application.create.user_create_command import UserCreateCommand
from src.context.user.application.search_all.user_list import UserList


class UserContainer(containers.DeclarativeContainer):

    # config = providers.Configuration(yaml_files=["application.yaml"])
    user_repository = providers.Singleton(
        SqlAlchemyUserRepository
    )

    user_creator = providers.Factory(
        UserCreator,
        repository=user_repository
    )

    user_create_command = providers.Factory(
        UserCreateCommand,
        creator=user_creator
    )

    user_list = providers.Factory(
        UserList,
        repository=user_repository
    )
