from .pattern import (
    AbstractCarBuilder,
    BaseBody,
    BaseCar,
    BaseEngine,
    BaseWheels,
)


class DieselCarBuilder(AbstractCarBuilder):
    """Строитель дизельного автомобиля"""

    @classmethod
    def build_engine(cls) -> BaseEngine:
        """Фабричный метод дизельного двигателя."""

        return BaseEngine(gas_type="Diesel")

    @classmethod
    def build_wheels(cls) -> BaseWheels:
        """Фабричный метод колес дизельного автомобиля."""

        return BaseWheels(diameter=22)

    @classmethod
    def build_body(cls) -> BaseBody:
        """Фабричный метод кузова дизельного двигателя."""

        return BaseBody(body_type="Jeep")

    def create_car(self) -> BaseCar:
        """Фабричный метод создания дизельного автомобиля."""

        return BaseCar(
            body=self.build_body(),
            engine=self.build_engine(),
            wheels=self.build_wheels(),
        )


class Driver:
    """Водитель, который будет управлять автомобилем."""

    def __init__(self, car: BaseCar) -> None:
        self._car = car

    def steady_ready_go(self) -> None:
        """Интерфейс управления автомобилем."""
        self._car.drive()
