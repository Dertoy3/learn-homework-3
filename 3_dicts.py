"""
Задание 3. Словари.

Данные корректны: age — целое число, churn — 0 или 1.
В main() создай минимум четыре словаря клиентов и проверь функции.
"""


def describe_client(client: dict) -> str:
    """Верни строку "Анна, 25 лет, город: Москва".
    Обязательные ключи: name, age. Если city отсутствует, используй "не указан".
    """
    if client.get('city') is None:
        return f'{client.get('name')}, {client.get('age')} лет, город: не указан'
    return f'{client.get('name')}, {client.get('age')} лет, город: {client.get('city')}'

from collections import Counter

def count_by_city(clients: list[dict]) -> dict:
    """Верни словарь: город -> число клиентов.
    У всех клиентов здесь есть ключ city.
    Для пустого списка верни {}. Исходные данные не изменяй.
    """
    client_count: dict = {}
    if clients:
        for d in clients:
            if (c:=d.get('city')) in client_count:
                client_count[c] += 1
            else:
                client_count[c] = 1
    return client_count


def get_departed_names(clients: list[dict]) -> list[str | None]:
    """Верни список имён клиентов с churn == 0 в исходном порядке.
    У каждого клиента есть name и churn. Для пустого списка верни [].
    """
    return [x.get('name') for x in clients if x.get('churn')==0]


def main():
    clients = [
        {"name": "Анна", "age": 25, "city": "Москва", "churn": 0},
        {"name": "Иван", "age": 32, "city": "Казань", "churn": 1},
        {"name": "Олег", "age": 40, "city": "Москва", "churn": 0},
        {"name": "Елена", "age": 28, "city": "Омск", "churn": 1},
    ]
    print("Клиент:", describe_client(clients[0]))
    print("Без города:", describe_client({"name": "Мария", "age": 35}))
    print("Клиенты по городам:", count_by_city(clients))
    print("Пустой список городов:", count_by_city([]))
    print("Ушедшие:", get_departed_names(clients))
    print("Нет клиентов:", get_departed_names([]))


if __name__ == "__main__":
    main()
