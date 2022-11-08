from typing import List

from abc import ABC, abstractmethod
from .user import User


class IUserRepository(ABC):

    @abstractmethod
    def save(self, user: User):
        raise NotImplementedError

    @abstractmethod
    def list_all(self) -> List[User]:
        raise NotImplementedError
