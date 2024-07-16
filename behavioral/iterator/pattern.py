from abc import ABC, abstractmethod


class AbstractIteratorNode(ABC):
    """Описание интерфейса абстрактного узла итератора."""

    def __init__(
        self,
        name_node: str,
        value_node: int,
        next_node: "AbstractIteratorNode | None" = None,
        prev_node: "AbstractIteratorNode | None" = None,
    ) -> None:
        self._name = name_node
        self._value = value_node
        self._next_node = next_node
        self._prev_node = prev_node

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

    @abstractmethod
    def print_current_node(self) -> None:
        """Вывод текущего узла на печать."""
        ...


class AbstractIterator(ABC):
    """Описание интерфейса абстрактного итератора."""

    def __init__(
        self, current_node: AbstractIteratorNode | None = None
    ) -> None:
        self._current_node = current_node

    @abstractmethod
    def set_current_node(self, current_node: AbstractIteratorNode) -> None:
        """Установка текущего узла для итератора."""
        ...

    @abstractmethod
    def __iter__(self) -> "AbstractIterator":
        """Интерфейс подготовки итератора."""
        ...

    @abstractmethod
    def __next__(self) -> AbstractIteratorNode:
        """Интерфейс обхода итерируемого объекта."""
        ...
