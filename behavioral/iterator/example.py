from typing import Generator

from .pattern import AbstractIterator, AbstractIteratorNode


class LinkedListNode(AbstractIteratorNode):
    """Узел связанного списка."""

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

    def print_current_node(self) -> None:
        print(self)


class LinkedListIterator(AbstractIterator):
    """Итератор связанного списка."""

    def __iter__(self) -> AbstractIterator:
        return self

    def __next__(self) -> AbstractIteratorNode:
        if self._current_node is None:
            raise StopIteration

        result = self._current_node
        self._current_node = self._current_node.next_node

        return result

    def set_current_node(self, current_node: AbstractIteratorNode) -> None:
        self._current_node = current_node


class LinkedListGenerator(AbstractIterator):
    """Генератор связанного списка."""

    def __init__(self, current_node: LinkedListNode | None = None) -> None:
        self._current_node = current_node

    def set_current_node(self, current_node: AbstractIteratorNode) -> None:
        self._current_node = current_node

    def __iter__(self) -> Generator[AbstractIteratorNode, None, None]:
        while True:
            result = self._current_node
            if self._current_node is None:
                break
            yield self._current_node

            if result is self._current_node:
                self._current_node = self._current_node.next_node

    def __next__(self) -> AbstractIteratorNode:
        raise NotImplementedError
