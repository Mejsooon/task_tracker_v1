from app.models.models import User
from app.repositories import user_repository


def authenticate(username: str, password: str):
    user = user_repository.find_by_username(username)
    if user and user.password == password:
        return user
    return None
