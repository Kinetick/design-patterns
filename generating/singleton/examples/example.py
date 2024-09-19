from ..pattern.base import (
    BaseMetaSingleton,
    BaseNewSingleton,
    BaseThreadSafeSingleton,
    singleton,
)


@singleton
class DecoratorSingleton:
    """Пример использования паттерна через декоратор одиночки."""

    ...


class NewSingleton(BaseNewSingleton):
    """Пример использования паттерна через перегрузку __new__."""

    ...


class MetaSingleton(metaclass=BaseMetaSingleton):
    """Пример использования паттерна через метакласс."""

    ...


class ThreadSingleton(metaclass=BaseThreadSafeSingleton):
    """Пример использования паттерна thread safe через метакласс."""

    ...
