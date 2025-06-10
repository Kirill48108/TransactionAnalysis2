def write_to_file_decorator(filename):

    def decorator(func):

        def wrapper(*args, **kwargs):

            result = func(*args, **kwargs)

            with open(filename, "a") as f:

                f.write(f"Result: {result}\n")

            return result

        return wrapper

    return decorator


# Пример использования декоратора


@write_to_file_decorator("output.txt")
def add(a, b):

    return a + b


from unittest.mock import mock_open, patch

import pytest

from src.decorators import decorator_record_file

# Импортируйте ваш декоратор



def test_write_to_file_decorator():
    # Создаем мок для функции open

    mock_file = mock_open()

    with patch("builtins.open", mock_file):
        # Вызовем декорированную функцию

        result = add(3, 5)

        # Проверим, что функция вернула правильный результат

        assert result == 8

        # Проверим, что функция open была вызвана с правильным именем файла

        mock_file.assert_called_once_with("output.txt", "a")

        # Проверим, что в файл было записано правильное значение

        mock_file().write.assert_called_once_with("Result: 8\n")
