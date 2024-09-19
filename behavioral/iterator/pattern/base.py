from typing import Generator

from .abc import AbstractIterator, AbstractIteratorNode, T


class BaseIteratorNode(AbstractIteratorNode):
    """Базовый класс узла итератора."""

    def __init__(
        self,
        name_node: str,
        value_node: int,
        next_node: AbstractIteratorNode | None = None,
        prev_node: AbstractIteratorNode | None = None,
    ) -> None:
        self._name = name_node
        self._value = value_node
        self._next_node = next_node
        self._prev_node = prev_node

    @property
    def next_node(self) -> AbstractIteratorNode | None:
        return self._next_node

    def set_prev_node(self, prev_node: AbstractIteratorNode | None) -> None:
        self._prev_node = prev_node

    def set_next_node(self, next_node: AbstractIteratorNode | None) -> None:
        self._next_node = next_node

    def __str__(self) -> str:
        description = f"""
            Имя узла: {self._name}
            Значение узла: {self._value}
            Есть предыдущий: {bool(self._prev_node)}
            Есть следующий: {bool(self._next_node)}
        """

        return description


class BaseIterator(AbstractIterator[T]):
    """Базовый класс итератора."""

    def __init__(self, current_node: T | None = None) -> None:
        self._current_node = current_node

    def set_current_node(self, current_node: T) -> None:
        self._current_node = current_node


class BaseNodesIterator(BaseIterator[T]):
    """Базовый итератор узлов."""

    def __iter__(self) -> AbstractIterator[T]:
        return self

    def __next__(self) -> T:
        if self._current_node is None:
            raise StopIteration

        result = self._current_node
        self._current_node = self._current_node.next_node

        return result


class BaseNodesGenerator(BaseIterator[T]):
    """Базовый генератор узлов."""

    def __iter__(self) -> Generator[T, None, None]:
        while True:
            result = self._current_node
            if self._current_node is None:
                raise StopIteration
            yield self._current_node

            if result is self._current_node:
                self._current_node = self._current_node.next_node

    def __next__(self) -> T:
        raise NotImplementedError
