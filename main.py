from fastapi import FastAPI

from src.app.user.routes import router as user_route

app = FastAPI()


app.include_router(user_route)
