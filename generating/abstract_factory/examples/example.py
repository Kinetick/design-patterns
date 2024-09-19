from ..pattern.abc import AbstractVehicleFactory
from ..pattern.base import (
    BaseCar,
    BaseDriver,
    BaseMotorCycle,
)


class YamahaVehicleFactory(AbstractVehicleFactory):
    """Пример использования фабрики для транспорта Yamaha."""

    @classmethod
    def create_car(cls) -> BaseCar:
        vehicle = BaseCar(
            producer_name="Yamaha", doors_count=4, horse_powers=120
        )

        return vehicle

    @classmethod
    def create_motorcycle(cls) -> BaseMotorCycle:
        vehicle = BaseMotorCycle(producer_name="Yamaha", horse_powers=200)

        return vehicle


class HondaVehicleFactory(AbstractVehicleFactory):
    """Пример использования фабрики для транспорта Honda."""

    @classmethod
    def create_car(cls) -> BaseCar:
        vehicle = BaseCar(
            producer_name="Honda", doors_count=2, horse_powers=140
        )

        return vehicle

    @classmethod
    def create_motorcycle(cls) -> BaseMotorCycle:
        vehicle = BaseMotorCycle(producer_name="Honda", horse_powers=225)

        return vehicle


common_driver = BaseDriver(vehicle_factory=YamahaVehicleFactory())
common_driver.current_factory = HondaVehicleFactory()
