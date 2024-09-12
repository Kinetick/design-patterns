from abc import ABC, abstractmethod
from typing import Type


class AbstractExpression(ABC):
    """Описание интерфейса абстрактного выражения."""

    @abstractmethod
    def interpret(self):
        """Интерфейс запуска интерпретации выражения."""
        ...


class AbstractArithmeticPrioritiesRepo(ABC):
    """Описание интерфейса репозитория приоритетов арифметических операций."""

    def register_level(
        self, level: dict[str, Type["BaseArithmeticExpression"]]
    ) -> None:
        """Интерфейс добавления уровня приоритетов в репозиторий."""
        ...

    def get_level(
        self, index: int
    ) -> dict[str, Type["BaseArithmeticExpression"]]:
        """Интерфейс получения уровня приоритетов арифметических операций."""
        ...


class BaseNumericExpression(AbstractExpression):
    """Описание интерфейса терминального выражения (числа)."""

    def __init__(self, expression: str) -> None:
        self._expression = expression

    def interpret(self):
        return float(self._expression)


class BaseArithmeticExpression(AbstractExpression):
    """Описание интерфейса нетерминального выражения (ариф. операция)."""

    def __init__(
        self,
        left_expression: BaseNumericExpression,
        right_expression: BaseNumericExpression,
    ) -> None:
        self._left_expression = left_expression
        self._right_expression = right_expression


class BaseArithmeticPrioritiesRepo(AbstractArithmeticPrioritiesRepo):
    """Базовый класс репозитория приоритетов операций."""

    def __init__(
        self,
    ) -> None:
        self._map_prior: dict[
            int, dict[str, Type[BaseArithmeticExpression]]
        ] = {}
        self.last_level_index = 0

    def register_level(
        self, level: dict[str, Type[BaseArithmeticExpression]]
    ) -> None:
        self._map_prior[self.last_level_index] = level
        self.last_level_index += 1

    def get_level(
        self, index: int
    ) -> dict[str, Type[BaseArithmeticExpression]]:
        return self._map_prior[index]
