from .pattern import (
    AbstractHouse,
    AbstractHouseCaretaker,
    HouseMemento,
)


class SimpleHouse(AbstractHouse):
    def __init__(self) -> None:
        self._rooms_count = 0
        self._windows_count = 0
        self._roof_existence = False
        self._fundament_existence = False
        self._box_existence = False

    def build_box(self) -> None:
        self._box_existence = True

    def destroy_box(self) -> None:
        self._box_existence = False

    def build_fundament(self) -> None:
        self._fundament_existence = True

    def destroy_fundament(self) -> None:
        self._fundament_existence = False

    def build_roof(self) -> None:
        self._roof_existence = True

    def destroy_roof(self) -> None:
        self._roof_existence = False

    def build_room(self) -> None:
        self._rooms_count += 1

    def destroy_room(self) -> None:
        if self._rooms_count > 0:
            self._rooms_count -= 1

    def build_window(self) -> None:
        self._windows_count += 1

    def destroy_window(self) -> None:
        if self._windows_count > 0:
            self._windows_count -= 1

    def create_memento(self) -> HouseMemento:
        return HouseMemento(
            roof_existence=self._roof_existence,
            fundament_existence=self._fundament_existence,
            box_existence=self._box_existence,
            windows_count=self._windows_count,
            rooms_count=self._rooms_count,
        )

    def load_memento(self, memento: HouseMemento):
        self._roof_existence = memento.roof_existence
        self._fundament_existence = memento.fundament_existence
        self._box_existence = memento.box_existence
        self._rooms_count = memento.rooms_count
        self._windows_count = memento.windows_count

    def __str__(self) -> str:
        description = f"""
            Кол-во комнат: {self._rooms_count}
            Кол-во окон: {self._windows_count}
            Есть крыша: {self._roof_existence}
            Есть фундамент: {self._fundament_existence}
            Есть несущие стены: {self._box_existence}
        """

        return description


class SimpleHouseCaretaker(AbstractHouseCaretaker):
    def recovery_state(self, index: int) -> None:
        try:
            self._house.load_memento(self._mementos[index])
        except IndexError:
            print(f'Отсутствует снимок состояния по индексом: {index}.')
        finally:
            print(self._house)

    def save_state(self) -> None:
        self._mementos.append(self._house.create_memento())
        index = len(self._mementos) - 1
        print(f"Снимок состояния сохранен под индексом: {index}.")
