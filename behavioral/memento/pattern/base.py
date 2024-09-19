from typing import Type

from .abc import (
    HT,
    MT,
    AbstractHouse,
    AbstractHouseCaretaker,
)


def load_memento_data(memento_type: Type[MT], load_data: dict) -> MT:
    """Функция заполнения модели снимка данными."""
    required_data = {
        key: load_data[key] for key in memento_type.__required_keys__
    }
    not_required_data = {
        key: load_data[key]
        for key in memento_type.__optional_keys__
        if key in load_data
    }

    return memento_type(**(required_data | not_required_data))


class BaseHouse(AbstractHouse[MT]):
    """Базовый класс дома."""

    def __init__(
        self,
        memento_type: Type[MT],
        rooms_count: int = 0,
        windows_count: int = 0,
        roof_existence: bool = False,
        fundament_existence: bool = False,
        box_existence: bool = False,
    ) -> None:
        self._rooms_count = rooms_count
        self._windows_count = windows_count
        self._roof_existence = roof_existence
        self._fundament_existence = fundament_existence
        self._box_existence = box_existence
        self._memento_type = memento_type

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

    def create_memento(self) -> MT:
        memento_data = {
            "roof_existence": self._roof_existence,
            "fundament_existence": self._fundament_existence,
            "box_existence": self._box_existence,
            "rooms_count": self._rooms_count,
            "windows_count": self._windows_count,
        }

        return load_memento_data(
            memento_type=self._memento_type, load_data=memento_data
        )

    def load_memento(self, memento: MT):
        required_fields = set(self._memento_type.__required_keys__)
        optional_fields = set(self._memento_type.__optional_keys__)
        memento_fields = set(memento.keys())

        if not required_fields.issubset(memento_fields):
            raise KeyError("В снимке состояния отсутствуют обязательные поля!")

        for key in required_fields | optional_fields:
            if key in memento:
                setattr(self, f"_{key}", memento.get(key))

    def __str__(self) -> str:
        description = f"""
            Кол-во комнат: {self._rooms_count}
            Кол-во окон: {self._windows_count}
            Есть крыша: {self._roof_existence}
            Есть фундамент: {self._fundament_existence}
            Есть несущие стены: {self._box_existence}
        """

        return description


class BaseHouseCaretaker(AbstractHouseCaretaker[HT, MT]):
    """Базовый класс хранителя дома?"""

    def __init__(self, house: AbstractHouse[MT]) -> None:
        self._house = house
        self._mementos: list[MT] = []

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
