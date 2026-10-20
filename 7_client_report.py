from typing import TypedDict
"""
Задание 7. Итоговая задача: отчёт по клиентам.

Важно: churn = 0 — ушёл; churn = 1 — остался.
Данные корректны, все ключи присутствуют.

Реализуй функции так, чтобы build_report использовала вспомогательные функции.
Не используй pandas, global и изменение исходных данных.

Для CLIENTS в build_report ожидается:
total = 5
departed_count = 3
departed_share = 0.6 (доля от 0 до 1, не процент)
departed_names = ["Анна", "Олег", "Мария"]
cities = {"Москва", "Казань", "Омск"} (множество)
departed_by_city = {"Москва": 2, "Казань": 0, "Омск": 1}

Для пустого списка:
total и departed_count = 0, departed_share = 0.0;
departed_names = [], cities = set(), departed_by_city = {}.

В main() построй и выведи отчёт для CLIENTS и для [].
Для каждого шага объясни, почему выбран список, словарь или множество.
"""

class Client(TypedDict):
    name: str
    age: int
    city: str
    churn: int


CLIENTS: list[Client] = [
    {"name": "Анна", "age": 25, "city": "Москва", "churn": 0},
    {"name": "Иван", "age": 32, "city": "Казань", "churn": 1},
    {"name": "Олег", "age": 40, "city": "Москва", "churn": 0},
    {"name": "Елена", "age": 28, "city": "Омск", "churn": 1},
    {"name": "Мария", "age": 35, "city": "Омск", "churn": 0},
]

def get_departed(clients: list[Client]) -> list:
    """Верни список словарей ушедших клиентов в исходном порядке."""
    return [x for x in clients if x.get('churn') == 0]


def calculate_departed_share(clients: list[Client], departed: int) -> float:
    """Верни долю ушедших среди всех клиентов. Для [] верни 0.0."""
    if departed == 0:
        return 0.0
    return 1/len(clients)*departed


def count_departed_by_city(clients: list[Client]) -> dict:
    """Верни словарь город -> число ушедших.
    Включи каждый город из clients, даже если ушедших в нём нет.
    """
    departed_by_city = {}
    for client in clients:
        city = client.get('city')
        churn = client.get('churn')

        if city in departed_by_city and churn == 0:
            departed_by_city[city] += 1
        elif churn == 1:
            departed_by_city[city] = 0
        else:
            departed_by_city[city] = 1
    return departed_by_city


def build_report(clients: list[Client]) -> dict:
    """Верни словарь с шестью ключами, перечисленными в условии."""
    departed = get_departed(clients)
    departed_names = [x.get('name') for x in departed]
    departed_count = len(departed)
    cities = {x.get('city') for x in clients}
    return {
        'total': len(clients),
        'departed_count': departed_count,
        'departed_share': calculate_departed_share(clients, departed_count),
        'departed_names': departed_names,
        'cities': cities,
        'departed_by_city': count_departed_by_city(clients)
    }


def main():
    print("Отчёт по клиентам:", build_report(CLIENTS))
    print("Отчёт без клиентов:", build_report([]))


if __name__ == "__main__":
    main()
