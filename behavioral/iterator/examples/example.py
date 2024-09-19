from ..pattern.base import (
    BaseIteratorNode,
    BaseNodesGenerator,
    BaseNodesIterator,
)


class LinkedListNode(BaseIteratorNode):
    """Узел связанного списка."""

    ...


test_node_1 = LinkedListNode(name_node="1", value_node=1)
test_node_2 = LinkedListNode(name_node="2", value_node=2)
test_node_3 = LinkedListNode(name_node="3", value_node=3)
test_node_4 = LinkedListNode(name_node="4", value_node=4)
test_node_1.set_next_node(next_node=test_node_2)
test_node_2.set_next_node(next_node=test_node_3)
test_node_2.set_prev_node(prev_node=test_node_1)
test_node_3.set_next_node(next_node=test_node_4)
test_node_3.set_prev_node(prev_node=test_node_2)
test_node_4.set_prev_node(prev_node=test_node_3)

common_iterator = BaseNodesIterator[LinkedListNode](current_node=test_node_1)
common_generator = BaseNodesGenerator[LinkedListNode](current_node=test_node_1)
