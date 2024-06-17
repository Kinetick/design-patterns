from .pattern import AbstractVehicleFactory


class Driver:
    """Класс водителя, который будет использовать технику."""

    def __init__(self, vehicle_factory: AbstractVehicleFactory) -> None:
        self._vehicle_factory = vehicle_factory

    def presentation(self) -> None:
        """Презентация техники от бренда."""

        presentation = f"""
            Автомобиль:
                {self._vehicle_factory.create_car()}

            Мотоцикл:
                {self._vehicle_factory.create_motorcycle()}
        """
        print(presentation)
