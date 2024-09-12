from .pattern import BaseHouse, BaseHouseCaretaker


class SimpleHouse(BaseHouse):

    def add_box(self) -> None:
        self._box_existence = True

    def remove_box(self) -> None:
        self._box_existence = False

    def add_fundament(self) -> None:
        self._fundament_existence = True

    def remove_fundament(self) -> None:
        self._fundament_existence = False

    def add_roof(self) -> None:
        self._roof_existence = True

    def remove_roof(self) -> None:
        self._roof_existence = False

    def add_room(self) -> None:
        self._rooms_count += 1

    def remove_room(self) -> None:
        if self._rooms_count > 0:
            self._rooms_count -= 1

    def add_window(self) -> None:
        self._windows_count += 1

    def remove_window(self) -> None:
        if self._windows_count > 0:
            self._windows_count -= 1


class SimpleHouseCaretaker(BaseHouseCaretaker):
    """Простой хранитель, простого дома)"""
