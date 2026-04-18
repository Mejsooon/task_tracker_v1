from app.models.models import Task
from app.core.database import store


def save(task: Task):
    if task not in store.users:
        store.users.append(task)