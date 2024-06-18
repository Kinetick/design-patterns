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
        """Абстрактный, фабричный метод создания автомобиля."""
        ...

    @abstractmethod
    def create_motorcycle(cls) -> BaseMotorCycle:
        """Абстрактный, фабричный метод создания мотоцикла."""
        ...


class YamahaVehicleFactory(AbstractVehicleFactory):
    """Фабрика производства транспорта Yamaha."""

    @classmethod
    def create_car(cls) -> BaseCar:
        """Фабричный метод создания автомобиля Yamaha."""
        vehicle = BaseCar(
            producer_name="Yamaha", doors_count=4, horse_powers=120
        )

        return vehicle

    @classmethod
    def create_motorcycle(cls) -> BaseMotorCycle:
        """Фабричный метод создания мотоцикла Yamaha."""
        vehicle = BaseMotorCycle(producer_name="Yamaha", horse_powers=200)

        return vehicle


class HondaVehicleFactory(AbstractVehicleFactory):
    """Фабрика производства транспорта Honda."""

    @classmethod
    def create_car(cls) -> BaseCar:
        """Фабричный метод создания автомобиля Honda."""
        vehicle = BaseCar(
            producer_name="Honda", doors_count=2, horse_powers=140
        )

        return vehicle

    @classmethod
    def create_motorcycle(cls) -> BaseMotorCycle:
        """Фабричный метод создания мотоцикла Honda."""
        vehicle = BaseMotorCycle(producer_name="Honda", horse_powers=225)

        return vehicle
