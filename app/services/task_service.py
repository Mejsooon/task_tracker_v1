from app.models.models import User, Task
from app.core.database import store
from app.utils.helpers import get_next_id
from app.repositories import task_repository


def create_task(user: User, difficulty: int, description: str ) -> tuple[bool, str]:
    if not (1 <= difficulty <= 10):
        return None, "❌ Poziom trudności musi być między 1 a 10."
    if not description:
        return None, "❌ Wszystkie pola są wymagane"

    new_task = Task(
        id=get_next_id("T", store.tasks),
        user_id=user.id,
        task_difficulty=difficulty,
        task_description=description,
    )

    task_repository.save(new_task)
    return True, f"Zadanie {new_task.id} zostało poprawnie utworzone."