from typing import Optional, List
from app.models.models import User, Task

class DataStore:
    def __init__(self):
        self.users: List[User] = []
        self.tasks: List[Task] = []

    def _init_demo_users(self):
        self.users.append(User(
            id="U001",
            name="Jan Kowalski",
            username="user1",
            password="Pass123"
        ))

    _init_demo_users()

store = DataStore() # Przypisanie bazy danych do zmiennej