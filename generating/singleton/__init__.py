"""
Порождающий паттерн проектирования - одиночка.

pattern.py
    Паттерн используется для предоставления единственного экземпляра класса.
    Каждый вызов инициализатора, всегда будет возвращать один и тот же
    экземпляр.

example.py
    В файле будет приведено несколько примеров:
        - реализация паттерна при помощи метода __new__
        - реализация паттерна при помощи декоратора
        - реализация паттерна при помощи метакласса
        - реализация thread safe одиночки.
"""

from .example import (
    DecoratorSingletonExample,
    MetaClassSingletonExample,
    NewMethodSingletonExample,
    ThreadSafeSingletonExample,
)

__all__ = [
    "DecoratorSingletonExample",
    "MetaClassSingletonExample",
    "NewMethodSingletonExample",
    "ThreadSafeSingletonExample",
]
