from .pattern import (
    MetaClassSingleton,
    NewMethodSingleton,
    ThreadSafeSingleton,
    singleton,
)


@singleton
class DecoratorSingleton:
    """Класс для примера реализации через декоратор класса."""

    ...


class NewSingleton(NewMethodSingleton):
    """Класс для примера реализации через перегрузку __new__."""

    ...


class MetaSingleton(metaclass=MetaClassSingleton):
    """Класс для примера реализации через метакласс."""

    ...


class ThreadSingleton(metaclass=ThreadSafeSingleton):
    """Класс для примера реализации thread safe через метакласс."""

    ...
