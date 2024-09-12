from typing import Generator

from .pattern import BaseIterator, BaseIteratorNode


class LinkedListNode(BaseIteratorNode):
    """Узел связанного списка."""


class LinkedListIterator(BaseIterator):
    """Итератор связанного списка."""

    def __iter__(self) -> BaseIterator:
        return self

    def __next__(self) -> BaseIteratorNode:
        if self._current_node is None:
            raise StopIteration

        result = self._current_node
        self._current_node = self._current_node.next_node

        return result


class LinkedListGenerator(BaseIterator):
    """Генератор связанного списка."""

    def __iter__(self) -> Generator[BaseIteratorNode, None, None]:
        while True:
            result = self._current_node
            if self._current_node is None:
                raise StopIteration
            yield self._current_node

            if result is self._current_node:
                self._current_node = self._current_node.next_node

    def __next__(self) -> BaseIteratorNode:
        raise NotImplementedError
