from app.models.models import User
from app.utils.helpers import clear_screen, read_multiline
from app.services import task_service

def user_panel(user: User):
    while True:
        clear_screen()
        print(f"PROFIL UŻYTKOWNIKA: {user.name}")
        print("(1) Utwórz nowe zadanie")
        print("(2) Aktywne zadania")
        print("(3) Histori zadań")
        print("(4) Wyloguj się")

        user_choice = input("Wybierz opcję: ")

        if user_choice == "1":
            pass # _create_task
        elif user_choice == "2":
            pass # _active_task
        elif user_choice == "3":
            pass # _task_history
        elif user_choice == "4":
            break
        else:
            print("\n❌ Nieprawidłowa opcja.")
            input("\nNaciśnij Enter...")


def _create_task(user: User):
    clear_screen()
    print("NOWE ZADANIE EKSPOZYCYJNE")
    print("=" * 60)

    try:
        difficulty = int(input("Trudność zadania (1-10): ").strip())
    except ValueError:
        difficulty = 0

    description = read_multiline("Opis zadania (zakończ pustą linią): ")

    ok, msg = task_service.create_task(user, difficulty, description)
    print(f"\n{'✅' if ok else '❌'} {msg}")
    input("\nNaciśnij Enter...")