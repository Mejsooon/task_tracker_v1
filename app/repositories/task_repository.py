from app.models.models import Task
from app.core.database import store


def save(task: Task):
    if task not in store.users:
        store.tasks.append(task)


def find_by_id_and_status(user_id: str, status: str):
    return [t for t in store.tasks if t.user_id == user_id and t.status == status]