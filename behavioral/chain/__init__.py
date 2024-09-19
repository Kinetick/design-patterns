"""
Поведенческий паттерн - цепочка обязанностей.

О паттерне:
    Паттерн позволяет делегировать запрос цепочке обработчиков. При этом не
    известно сколько этих самых обработчиков есть в цепочке. Каждый обработчик
    на месте решает, отправить запрос дальше или прервать обработку.

Пример:
    В качестве примера рассмотрим простой валидатор вводимого пользователем
    пароля. Валидным будет считать пароль, который отвечает следующим
    требованиям:
        - длина не менее 10 символов
        - есть как строчные, так и прописные буквы
        - в теле есть спецсимволы
        - в теле есть цифры
"""
