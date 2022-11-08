from ...domain.abstract_user_repository import IUserRepository
# from ...infrastructure.sqlalchemy_user_repository import SqlAlchemyUserRepository


class UserList:

    def __init__(self, repository: IUserRepository):
        self._repository: IUserRepository = repository

    def run(self):
        return [user.to_json() for user in self._repository.list_all()]