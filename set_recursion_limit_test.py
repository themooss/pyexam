import sys

try:
    sys.setrecursionlimit(1000000000)  # Попробуйте большее значение
    print(f"Успешно установлено новое ограничение рекурсии: {sys.getrecursionlimit()}")
except RecursionError as e:
    print(f"Не удалось установить ограничение рекурсии: {e}")
except Exception as e:
    print(f"Другая ошибка: {e}")

