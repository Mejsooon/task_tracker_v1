from app.core.database import store
from app.models.models import User
from typing import Optional


def find_by_username(username: str) -> Optional[User]:
    return next((u for u in store.users if u.username == username), None)