from typing import List
from app.models.models import User, Task

class DataStore:
    def __init__(self):
        self.users: List[User] = []
        self.tasks: List[Task] = []
        self._init_demo_users()

    def _init_demo_users(self):
        self.users.append(User(
            id="U001",
            name="Jan Kowalski",
            username="user1",
            password="pass123"
        ))

store = DataStore() # Przypisanie bazy danych do zmiennej