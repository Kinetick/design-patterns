from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .base import ARITHMETIC_LEVELS


class AbstractExpression(ABC):
    """Описание интерфейса абстрактного выражения."""

    @abstractmethod
    def interpret(self) -> Any:
        """Интерфейс запуска интерпретации выражения."""
        ...


class AbstractArithmeticPrioritiesRepo(ABC):
    """Описание интерфейса репозитория приоритетов арифметических операций."""

    @property
    @abstractmethod
    def last_index(self) -> int:
        """Индекс последнего по приоритету уровня."""
        ...

    @abstractmethod
    def register_level(self, level: "ARITHMETIC_LEVELS") -> None:
        """Интерфейс добавления уровня приоритетов в репозиторий."""
        ...

    @abstractmethod
    def get_level(self, index: int) -> "ARITHMETIC_LEVELS":
        """Интерфейс получения уровня приоритетов арифметических операций."""
        ...


class AbstractApproximation(ABC):
    """Описание интерфейса аппроксиматора."""

    @abstractmethod
    def approximate(self, interpret_tokens: list[str]) -> list[str]:
        """Интерфейс инициации аппроксимации списка токенов"""
        ...
