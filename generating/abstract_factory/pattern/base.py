from .abc import AbstractDriver, AbstractVehicleFactory


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


class BaseDriver(AbstractDriver):
    """Базовый класс водителя."""

    def __init__(self, vehicle_factory: AbstractVehicleFactory) -> None:
        self._vehicle_factory = vehicle_factory

    @property
    def current_factory(self) -> AbstractVehicleFactory:
        """Текущий производитель транспорта."""
        return self._vehicle_factory

    @current_factory.setter
    def current_factory(self, new_factory: AbstractVehicleFactory) -> None:
        self._vehicle_factory = new_factory

    def start_presentation(self) -> None:
        presentation = f"""
            Автомобиль:
                {self._vehicle_factory.create_car()}

            Мотоцикл:
                {self._vehicle_factory.create_motorcycle()}
        """
        print(presentation)
