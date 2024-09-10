from .pattern import (
    AbstractVehicleFactory,
    BaseCar,
    BaseMotorCycle,
)


class YamahaVehicleFactory(AbstractVehicleFactory):
    """Фабрика производства транспорта Yamaha."""

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
    """Фабрика производства транспорта Honda."""

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


class Driver:
    """Класс водителя, который будет использовать технику."""

    def __init__(self, vehicle_factory: AbstractVehicleFactory) -> None:
        self._vehicle_factory = vehicle_factory

    def presentation(self) -> None:
        """Интерфейс презентации техники."""

        presentation = f"""
            Автомобиль:
                {self._vehicle_factory.create_car()}

            Мотоцикл:
                {self._vehicle_factory.create_motorcycle()}
        """
        print(presentation)
