from app.utils.helpers import clear_screen
from app.services import auth_service

def login_screen():
    clear_screen()
    print("\n" + "=" * 60)
    print("LOGOWANIE DO APLIKACJI")
    print("=" * 60)

    username = input("Wprowadź nazwę użytkownika: ")
    password = input("Wprowadź hasło: ")

    user = auth_service.authenticate(username, password)

    if not user:
        print("\n ❌Nieprawidłowa nazwa użytkownika, bądź hasło")
        print("\nNaciśnij Enter...")
        return

    print(f"\n✅ Witaj, {user.name}!")
    input("\nNaciśnij Enter, aby kontynuować...")
    return user
