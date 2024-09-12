from abc import ABC, abstractmethod


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


class AbstractIterator(ABC):
    """Описание интерфейса абстрактного итератора."""

    @abstractmethod
    def __iter__(self) -> "AbstractIterator":
        """Интерфейс подготовки итератора."""
        ...

    @abstractmethod
    def __next__(self) -> AbstractIteratorNode:
        """Интерфейс обхода итерируемого объекта."""
        ...


class BaseIteratorNode(AbstractIteratorNode):
    """Базовый класс узла итератора."""

    def __init__(
        self,
        name_node: str,
        value_node: int,
        next_node: "BaseIteratorNode | None" = None,
        prev_node: "BaseIteratorNode | None" = None,
    ) -> None:
        self._name = name_node
        self._value = value_node
        self._next_node = next_node
        self._prev_node = prev_node

    @property
    def next_node(self) -> "BaseIteratorNode | None":
        return self._next_node

    def set_prev_node(self, prev_node: "BaseIteratorNode | None") -> None:
        self._prev_node = prev_node

    def set_next_node(self, next_node: "BaseIteratorNode | None") -> None:
        self._next_node = next_node

    def __str__(self) -> str:
        description = f"""
            Имя узла: {self._name}
            Значение узла: {self._value}
            Есть предыдущий: {bool(self._prev_node)}
            Есть следующий: {bool(self._next_node)}
        """

        return description


class BaseIterator(AbstractIterator):
    """Базовый класс итератора."""

    def __init__(self, current_node: BaseIteratorNode | None = None) -> None:
        self._current_node = current_node

    @abstractmethod
    def set_current_node(self, current_node: BaseIteratorNode) -> None:
        """Установка текущего узла для итератора."""
        self._current_node = current_node
