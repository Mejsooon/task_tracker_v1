from dataclasses import dataclass

@dataclass
class User:
    id: str # U001, maksymalnie 1000 użytkowników
    name: str
    username: str
    password: str


@dataclass
class Task:
    id: str
    user_id: str # Do kogo przypisany jest ten task
    task_difficulty: str
    task_description: str
    status: str = "active"