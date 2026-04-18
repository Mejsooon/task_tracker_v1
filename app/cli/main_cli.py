from app.models.models import User
from app.utils.helpers import clear_screen

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