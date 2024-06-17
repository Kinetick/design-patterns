from .pattern import BaseCar


class Driver:
    """Водитель, который будет управлять автомобилем."""

    def __init__(self, car: BaseCar) -> None:
        self._car = car

    def steady_ready_go(self) -> None:
        """Интерфейс начала управления автомобилем."""
        self._car.drive()
