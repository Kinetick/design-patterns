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
    def build_room(self) -> None:
        """Интерфейс постройки комнаты."""
        ...

    @abstractmethod
    def destroy_room(self) -> None:
        """Интерфейс сноса комнаты."""
        ...

    @abstractmethod
    def build_window(self) -> None:
        """Интерфейс постройки окна."""
        ...

    @abstractmethod
    def destroy_window(self) -> None:
        """Интерфейс сноса окна."""
        ...

    @abstractmethod
    def build_fundament(self) -> None:
        """Интерфейс постройки фундамента."""
        ...

    @abstractmethod
    def destroy_fundament(self) -> None:
        """Интерфейс сноса фундамента."""
        ...

    @abstractmethod
    def build_roof(self) -> None:
        """Интерфейс постройки крыши."""
        ...

    @abstractmethod
    def destroy_roof(self) -> None:
        """Интерфейс сноса крыши."""
        ...

    @abstractmethod
    def build_box(self) -> None:
        """Интерфейс постройки короба."""
        ...

    @abstractmethod
    def destroy_box(self) -> None:
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

    def __init__(self, house: AbstractHouse) -> None:
        self._house = house
        self._mementos: list[HouseMemento] = []

    @abstractmethod
    def recovery_state(self, index: int) -> None:
        """Интерфейс восстановления состояния объекта."""
        ...

    @abstractmethod
    def save_state(self) -> None:
        """Сохранение состояния объекта."""
        ...
