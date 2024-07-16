"""
Поведенческий паттерн проектирования - хранитель.

pattern.py
    Паттерн позволяет сохранить и восстановить состояние объекта. Работа с
    состоянием происходит без нарушения инкапсуляции самого объекта. Более
    всего действие паттерна можно описать, как снимок текущего состояния
    с последующей загрузкой его в объект по требованию.

example.py
    В качестве примера рассмотрим процесс строительства дома. Для дома
    опишем интерфейс:
        - добавить комнату
        - убрать комнату
        - добавить окно
        - убрать окно
        - добавить крышу
        - построить наружный короб (стены)
        - построить фундамент
"""

from .example import SimpleHouse, SimpleHouseCaretaker

__all__ = ["SimpleHouseCaretaker", "SimpleHouse"]
