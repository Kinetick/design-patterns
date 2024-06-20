"""
Порождающий паттерн проектирования - прототип.

pattern.py
    Паттерн предоставляет интерфейс для клонирования объекта. Это востребовано
    в случаях, когда создание нового объекта менее выгодно и проще
    сделать копию существующего объекта.

    В питоне копирование объекта реализуется двумя функциями:
        - copy - вызывает метод __copy__ у объекта
        - deepcopy - вызывает метод __deepcopy__ у объекта
    Первый метод позволяет реализовать поверхностную копию, второй - глубокую.

example.py
    В качестве объекта возьмем ДВС. Создадим два варианта прототипа:
        - первый вариант будет использовать наследование для реализации
        - второй вариант будет регистрировать объекты и клонировать их
"""

from .example import (
    InheritanceInLineEngine,
    InheritanceRadialEngine,
    InheritanceVEngine,
    InLineEngine,
    RadialEngine,
    VEngine,
)
from .pattern import RegisterEnginePrototype

__all__ = [
    "InheritanceInLineEngine",
    "InheritanceRadialEngine",
    "InheritanceVEngine",
    "InLineEngine",
    "RadialEngine",
    "VEngine",
    "RegisterEnginePrototype",
]
