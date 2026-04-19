# Task Tracker (Python Console)

Simple task tracker with built-in database and console (UI) in (CLI)

---

### PROJECT STRUCTURE

- Structure based on **clean code architecture**
    - (services) as complete logic and (repositories) only for getting data from datbases

```bash
task_tracker_v1/
├── main.py
└── app/
    ├── models/
    │   └── models.py # @dataclasses
    ├── core/
    │   └── datastore.py # built-in database
    ├── utils/
    │   └── helpers.py
    ├── repositories/
    │   ├── user_repository.py
    │   ├── task_repository.py
    ├── services/
    │   ├── auth_service.py
    │   └── task_service.py
    └── cli/
        ├── auth_cli.py
        └── main_cli.py
```
---
### USEFUL FUNCTIONS:
- Multiline read function
```bash
def multiline_read(prompt: str = ""):
    if prompt:
        print(prompt)
    lines = []
    while True:
        line = input()
        if not line:
            break
        lines.append(line)
    return "\n".join(lines)
```
