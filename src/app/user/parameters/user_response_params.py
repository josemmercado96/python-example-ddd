from pydantic import BaseModel


class UserResponse(BaseModel):
    id: int
    username: str
    name: str
    last_name: str
    email: str
