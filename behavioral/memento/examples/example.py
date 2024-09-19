from ..pattern.abc import AbstractMemento
from ..pattern.base import BaseHouse, BaseHouseCaretaker


class SimpleMemento(AbstractMemento):
    """Снимок состояния простого дома."""

    roof_existence: bool
    fundament_existence: bool
    box_existence: bool
    rooms_count: int
    windows_count: int


simple_house = BaseHouse[SimpleMemento](memento_type=SimpleMemento)
simple_caretaker = BaseHouseCaretaker[BaseHouse[SimpleMemento], SimpleMemento](
    house=simple_house
)
