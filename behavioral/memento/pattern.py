from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass(frozen=True)
class HouseMemento:
    """Снимок состояния дома."""

    rooms_count: int
    windows_count: int
    fundament_existence: bool
    roof_existence: bool
    box_existence: bool


class AbstractHouse(ABC):
    """Описание интерфейса дома."""

    @abstractmethod
    def add_room(self) -> None:
        """Интерфейс постройки комнаты."""
        ...

    @abstractmethod
    def remove_room(self) -> None:
        """Интерфейс сноса комнаты."""
        ...

    @abstractmethod
    def add_window(self) -> None:
        """Интерфейс постройки окна."""
        ...

    @abstractmethod
    def remove_window(self) -> None:
        """Интерфейс сноса окна."""
        ...

    @abstractmethod
    def add_fundament(self) -> None:
        """Интерфейс постройки фундамента."""
        ...

    @abstractmethod
    def remove_fundament(self) -> None:
        """Интерфейс сноса фундамента."""
        ...

    @abstractmethod
    def add_roof(self) -> None:
        """Интерфейс постройки крыши."""
        ...

    @abstractmethod
    def remove_roof(self) -> None:
        """Интерфейс сноса крыши."""
        ...

    @abstractmethod
    def add_box(self) -> None:
        """Интерфейс постройки короба."""
        ...

    @abstractmethod
    def remove_box(self) -> None:
        """Интерфейс сноса короба."""
        ...

    @abstractmethod
    def create_memento(self) -> HouseMemento:
        """Интерфейс создания снимка состояния дома."""
        ...

    @abstractmethod
    def load_memento(self, memento: HouseMemento):
        """Интерфейс восстановления состояния дома со снимка."""
        ...


class AbstractHouseCaretaker(ABC):
    """Описание интерфейса обертки сохранения/восстановления состояния."""

    @abstractmethod
    def recovery_state(self, index: int) -> None:
        """Интерфейс восстановления состояния объекта."""
        ...

    @abstractmethod
    def save_state(self) -> None:
        """Сохранение состояния объекта."""
        ...


class BaseHouse(AbstractHouse):
    """Базовый класс дома."""

    def __init__(self) -> None:
        self._rooms_count = 0
        self._windows_count = 0
        self._roof_existence = False
        self._fundament_existence = False
        self._box_existence = False

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


class BaseHouseCaretaker(AbstractHouseCaretaker):
    """Базовый класс хранителя дома?"""

    def __init__(self, house: AbstractHouse) -> None:
        self._house = house
        self._mementos: list[HouseMemento] = []

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
