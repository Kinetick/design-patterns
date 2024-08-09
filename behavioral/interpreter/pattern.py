from abc import ABC, abstractmethod
from typing import Callable, Type


class AbstractExpression(ABC):
    """Описание интерфейса абстрактного выражения."""

    @abstractmethod
    def interpret(self):
        """Интерфейс запуска интерпретации выражения."""
        ...


class NumericExpression(AbstractExpression):
    """Описание интерфейса терминального выражения (числа)."""

    def __init__(self, expression: str) -> None:
        self._expression = expression

    def interpret(self):
        return float(self._expression)


class ArithmeticExpression(AbstractExpression):
    """Описание интерфейса нетерминального выражения (ариф. операция)."""

    def __init__(
        self,
        left_expression: NumericExpression,
        right_expression: NumericExpression,
    ) -> None:
        self._left_expression = left_expression
        self._right_expression = right_expression


class AddExpression(ArithmeticExpression):
    """Реализация интерпретации выражения сложения."""

    def interpret(self) -> float:
        return (
            self._left_expression.interpret()
            + self._right_expression.interpret()
        )


class SubExpression(ArithmeticExpression):
    """Реализация интерпретации выражения вычитания."""

    def interpret(self) -> float:
        return (
            self._left_expression.interpret()
            - self._right_expression.interpret()
        )


class DivExpression(ArithmeticExpression):
    """Реализация интерпретации выражения деления."""

    def interpret(self) -> float:
        return (
            self._left_expression.interpret()
            / self._right_expression.interpret()
        )


class MulExpression(ArithmeticExpression):
    """Реализация интерпретации выражения умножения."""

    def interpret(self) -> float:
        return (
            self._left_expression.interpret()
            * self._right_expression.interpret()
        )


class AbstractArithmeticPrioritiesRepo(ABC):
    """Описание интерфейса репозитория приоритетов арифметических операций."""

    def __init__(
        self,
    ) -> None:
        self._map_priorities: dict[
            int, dict[str, Type[ArithmeticExpression]]
        ] = {}
        self.last_level_index = 0

    def register_level(
        self, level: dict[str, Type[ArithmeticExpression]]
    ) -> None:
        """Интерфейс добавления уровня приоритетов в репозиторий."""
        ...

    def get_level(self, index: int) -> dict[str, Type[ArithmeticExpression]]:
        """Интерфейс получения уровня приоритетов арифметических операций."""
        ...


class BracketExpression(AbstractExpression):
    """Реализация интерпретации выражения скобок."""

    def __init__(
        self,
        expression: list[str],
        approximation_method: Callable[
            [list[str], AbstractArithmeticPrioritiesRepo], list[str]
        ],
        arithmetic_priorities_repo: AbstractArithmeticPrioritiesRepo,
    ):
        self._expression = expression
        self._approximation_method = approximation_method
        self._arithmetic_priorities_repo = arithmetic_priorities_repo

    def interpret(self) -> list[str]:
        self._expression = self._approximation_method(
            self._expression, self._arithmetic_priorities_repo
        )
        return self._expression
