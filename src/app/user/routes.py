from fastapi import APIRouter

from .parameters.user_response_params import UserResponse
from .parameters.user_create_params import UserParams

# from ...context.user.application.create.user_create_command import UserCreateCommand
# from ...context.user.application.search_all.user_list import UserList

from src.app.dependency_injection import UserContainer

container = UserContainer()

router = APIRouter(
    prefix="/api/v1/users",
    tags=["users"]
)


@router.get(
    path="/",
    response_model=list[UserResponse]
)
async def get_users():
    return container.user_list().run()


@router.post(
    path="/",
    response_model=dict
)
async def create_user(params: UserParams):
    return container.user_create_command().handle(params.dict())
