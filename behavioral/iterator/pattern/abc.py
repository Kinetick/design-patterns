from abc import ABC, abstractmethod
from typing import Generator, TypeVar

T = TypeVar("T", bound="AbstractIteratorNode")


class AbstractIteratorNode(ABC):
    """Описание интерфейса абстрактного узла итератора."""

    @property
    @abstractmethod
    def next_node(self) -> "AbstractIteratorNode | None":
        """Следующий узел в цепочке."""
        ...

    @abstractmethod
    def set_next_node(self, next_node: "AbstractIteratorNode | None") -> None:
        """Установка следующего узла в цепочке."""
        ...

    @abstractmethod
    def set_prev_node(self, prev_node: "AbstractIteratorNode | None") -> None:
        """Установка предыдущего узла в цепочке."""
        ...


class AbstractIterator[T](ABC):
    """Описание интерфейса абстрактного итератора."""

    @abstractmethod
    def set_current_node(self, current_node: T) -> None:
        """Интерфейс установки текущего узла."""
        ...

    @abstractmethod
    def __iter__(
        self,
    ) -> "AbstractIterator | Generator[T, None, None]":
        """Интерфейс подготовки итератора."""
        ...

    @abstractmethod
    def __next__(self) -> T:
        """Интерфейс обхода итерируемого объекта."""
        ...
