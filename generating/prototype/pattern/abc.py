from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, TypeVar

if TYPE_CHECKING:
    from .base import BaseCopier

T = TypeVar("T", bound="BaseCopier")


class AbstractRegisterPrototype[T](ABC):
    """Абстрактный класс"""

    @abstractmethod
    def register_copier(self, name_copier: str, copier: T) -> None:
        """Интерфейс регистрации копира."""
        ...

    @abstractmethod
    def unregister_copier(self, name_copier: str) -> T | None:
        """Интерфейс исключения копира."""
        ...

    @abstractmethod
    def clone(self, name_copier: str, is_shallow: bool) -> T:
        """Интерфейс инициации копирования через регистратор."""
        ...
