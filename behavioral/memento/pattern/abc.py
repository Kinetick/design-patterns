from abc import ABC, abstractmethod
from typing import TypedDict, TypeVar

MT = TypeVar("MT", bound="AbstractMemento")
HT = TypeVar("HT", bound="AbstractHouse")


# * Несколько абсурдно выглядит, т.к. сам TypedDict нельзя использовать для
# * ограничения типа, но производный класс - пожалуйста.
class AbstractMemento(TypedDict):
    """Абстрактный снимок состояния."""

    ...


class AbstractHouse[MT](ABC):
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
    def create_memento(self) -> MT:
        """Интерфейс создания снимка состояния дома."""
        ...

    @abstractmethod
    def load_memento(self, memento: MT):
        """Интерфейс восстановления состояния дома со снимка."""
        ...


class AbstractHouseCaretaker[HT, MT](ABC):
    """Описание интерфейса обертки сохранения/восстановления состояния."""

    @abstractmethod
    def recovery_state(self, index: int) -> None:
        """Интерфейс восстановления состояния объекта."""
        ...

    @abstractmethod
    def save_state(self) -> None:
        """Сохранение состояния объекта."""
        ...
