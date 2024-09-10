from abc import ABC, abstractmethod


class BaseCar:
    """Базовый класс автомобиля."""

    def __init__(
        self, producer_name: str, doors_count: int, horse_powers: int
    ) -> None:
        self._producer_name = producer_name
        self._doors_count = doors_count
        self._horse_powers = horse_powers

    def __str__(self) -> str:
        description = f"""
            Марка: {self._producer_name},
            Количество дверей: {self._doors_count},
            Мощность двигателя л/с: {self._horse_powers}
        """

        return description


class BaseMotorCycle:
    """Базовый класс мотоцикла."""

    def __init__(self, producer_name: str, horse_powers: int) -> None:
        self._producer_name = producer_name
        self._horse_powers = horse_powers

    def __str__(self) -> str:
        description = f"""
            Марка: {self._producer_name},
            Мощность двигателя л/с: {self._horse_powers}
        """

        return description


class AbstractVehicleFactory(ABC):
    """Абстрактная фабрика транспорта (машин и т.д.)."""

    @abstractmethod
    def create_car(cls) -> BaseCar:
        """Интерфейс создания автомобиля."""
        ...

    @abstractmethod
    def create_motorcycle(cls) -> BaseMotorCycle:
        """Интерфейс создания мотоцикла."""
        ...
