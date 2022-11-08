from .user_creator import UserCreator


class UserCreateCommand:

    def __init__(self, creator: UserCreator):
        self._creator = creator

    def handle(self, params: dict):
        return self._creator.run(params)

