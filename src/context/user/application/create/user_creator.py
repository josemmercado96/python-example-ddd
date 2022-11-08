from ...domain.user import User
from ...domain.abstract_user_repository import IUserRepository
# from ...infrastructure.sqlalchemy_user_repository import SqlAlchemyUserRepository


class UserCreator:

    def __init__(self, repository: IUserRepository):
        self._repository: IUserRepository = repository

    def run(self, params: dict) -> dict:
        user = User()
        user.username = params['username']
        user.password = params['password']
        user.name = params['name']
        user.last_name = params['last_name']
        user.email = params['email']
        self._repository.save(user)
        return user.to_json()
