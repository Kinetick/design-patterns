"""
Поведенческий паттерн проектирования - посетитель.

О паттерне:
    Паттерн позволяет добавлять новый функционал объектам или менять состояние
    объекта без изменения структуры класса объекта. Может применяться для
    разнородных объектов в определенном контексте.

Пример:
    Для примера рассмотрим набор бытовых приборов подключенных к общей шине
    домашней сети. В качестве приборов рассмотрим:
        - холодильник
        - чайник
        - стиральную машину

    Дополнительный функционал, который будет добавлен:
        - сводка базовых параметров прибора (метрическая система)
        - сводка базовых параметров прибора (американская система)
        - текущее состояние прибора (загрузка, включен и т.д.)
"""
