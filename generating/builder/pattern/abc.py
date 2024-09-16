"""."""

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .base import (
        BaseBody,
        BaseCar,
        BaseEngine,
        BaseWheels,
    )


class AbstractCarBuilder(ABC):
    """Абстрактный строитель автомобиля."""

    @classmethod
    @abstractmethod
    def build_wheels(cls) -> "BaseWheels":
        """Интерфейс создания колес автомобиля."""
        ...

    @classmethod
    @abstractmethod
    def build_engine(cls) -> "BaseEngine":
        """Интерфейс создания двигателя автомобиля."""
        ...

    @classmethod
    @abstractmethod
    def build_body(cls) -> "BaseBody":
        """Интерфейс создания кузова автомобиля."""
        ...

    # * По сути, интерфейс ниже может использовать "Шаблонный метод", т.к.
    # * логика создания автомобиля всегда одна.
    @abstractmethod
    def create_car(self) -> "BaseCar":
        """Интерфейс создания автомобиля."""
        ...


class AbstractCar(ABC):
    """Абстрактный автомобиль."""

    @abstractmethod
    def drive(self) -> None:
        """Интерфейс езды на автомобиле."""
        ...


class AbstractDriver(ABC):
    """Абстрактный водитель."""

    @abstractmethod
    def steady_ready_go(self, car: AbstractCar | None = None) -> None:
        """Интерфейс инициации езды на автомобиле."""
        ...
