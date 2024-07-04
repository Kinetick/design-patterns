"""
Поведенческий паттерн - цепочка обязанностей.

pattern.py
    Паттерн позволяет делегировать запрос цепочке обработчиков. При это не
    известно сколько этих самых обработчиков есть в цепочке. Каждый обработчик
    на месте решает, отправить запрос дальше или прервать обработку.

example.py
    В качестве примера рассмотрим простой валидатор вводимого пользователем
    пароля. Валидным будет считать пароль, который отвечает следующим
    требованиям:
        - длина не менее 10 символов
        - есть как строчные, так и прописные буквы
        - в теле есть спецсимволы
        - в теле есть цифры
"""

from .example import (
    PassCaseValidator,
    PassLengthValidator,
    PassNotAlphabeticalValidator,
    PassNotNumericalValidator,
    PassNotSpecialValidator,
    PassOnlyAlphabeticalValidator,
    PassOnlyNumericalValidator,
    PassOnlySpecialValidator,
)

__all__ = [
    "PassLengthValidator",
    "PassOnlyAlphabeticalValidator",
    "PassOnlyNumericalValidator",
    "PassOnlySpecialValidator",
    "PassCaseValidator",
    "PassNotAlphabeticalValidator",
    "PassNotNumericalValidator",
    "PassNotSpecialValidator",
]
