from .pattern import (
    MetaClassSingleton,
    NewMethodSingleton,
    ThreadSafeSingleton,
    singleton,
)


@singleton
class DecoratorSingletonExample:
    """Класс для примера реализации через декоратор класса."""

    ...


class NewMethodSingletonExample(NewMethodSingleton):
    """Класс для примера реализации через перегрузку __new__."""

    ...


class MetaClassSingletonExample(metaclass=MetaClassSingleton):
    """Класс для примера реализации через метакласс."""

    ...


class ThreadSafeSingletonExample(metaclass=ThreadSafeSingleton):
    """Класс для примера реализации thread safe через метакласс."""

    ...
