def clear_screen():
    print("\n" * 10)


def get_next_id(prefix: str, items: list):
    if not items:
        return f"{prefix}001"

    only_numbers = []
    for item in items:
        if item.id.startswith(prefix):
            only_numbers.append(int(item.id[1:])) # Wycinam pierwszy znak (U) i zwracam samą liczbę

    max_number = max(only_numbers)
    return f"{prefix}{max_number + 1:03d}"