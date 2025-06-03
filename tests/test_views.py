import json
from datetime import datetime

import pytest

from src.views import user_transactions, website


def test_website1():
    """Тестирование правильности работы функции"""
    data_time = datetime.now()
    result = website(data_time)

    # Проверь, что результат имеет ожидаемый тип и значения
    assert isinstance(result, tuple)
    assert len(result) == 5

    # Добавь дополнительные проверки для каждого из result1, result2 и т.д.
    # Например, если ожидается, что первый элемент - строка:
    assert isinstance(result[0], str)
