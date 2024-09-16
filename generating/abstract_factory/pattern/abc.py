from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .base import BaseCar, BaseMotorCycle


class AbstractVehicleFactory(ABC):
    """Абстрактная фабрика транспорта (машин и т.д.)."""

    @classmethod
    @abstractmethod
    def create_car(cls) -> "BaseCar":
        """Интерфейс создания автомобиля."""
        ...

    @classmethod
    @abstractmethod
    def create_motorcycle(cls) -> "BaseMotorCycle":
        """Интерфейс создания мотоцикла."""
        ...


class AbstractDriver(ABC):
    """Абстрактный водитель."""

    @abstractmethod
    def start_presentation(self) -> None:
        """Интерфейс запуска презентации"""
        ...
