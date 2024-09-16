from .abc import (
    AbstractCar,
    AbstractCarBuilder,
    AbstractDriver,
)


class BaseEngine:
    """Базовый класс двигателя."""

    def __init__(self, gas_type: str = "gasoline") -> None:
        self._gas_type = gas_type

    def __str__(self) -> str:
        description = f"""
            Тип топлива: {self._gas_type}
        """

        return description


class BaseWheels:
    """Базовый класс колес."""

    def __init__(self, diameter: int = 22) -> None:
        self._diameter = diameter

    def __str__(self) -> str:
        description = f"""
            Диаметр колес, см: {self._diameter}
        """

        return description


class BaseBody:
    """Базовый класс кузова."""

    def __init__(self, body_type: str = "sedan") -> None:
        self._body_type = body_type

    def __str__(self) -> str:
        description = f"""
            Тип кузова: {self._body_type}
        """

        return description


class BaseCar(AbstractCar):
    """Базовый класс автомобиля."""

    def __init__(
        self, body: BaseBody, engine: BaseEngine, wheels: BaseWheels
    ) -> None:
        self._engine = engine
        self._body = body
        self._wheels = wheels

    def __str__(self) -> str:
        description = f"""
            Об автомобиле:
                {self._engine}
                {self._body}
                {self._wheels}
        """

        return description

    def drive(self) -> None:
        """Интерфейс управления автомобилем."""
        print(self, "Погнали - ВРУУУУУМММ!", sep="\n")


class BaseCarBuilder(AbstractCarBuilder):
    @classmethod
    def build_body(cls) -> BaseBody:
        return BaseBody()

    @classmethod
    def build_engine(cls) -> BaseEngine:
        return BaseEngine()

    @classmethod
    def build_wheels(cls) -> BaseWheels:
        return BaseWheels()

    def create_car(self) -> BaseCar:
        return BaseCar(
            body=self.build_body(),
            wheels=self.build_wheels(),
            engine=self.build_engine(),
        )


class BaseDriver(AbstractDriver):
    """Базовый класс водителя."""

    def __init__(self, car_builder: AbstractCarBuilder) -> None:
        self._car_builder = car_builder

    @property
    def current_builder(self) -> AbstractCarBuilder:
        """Текущий строитель автомобиля."""
        return self._car_builder

    @current_builder.setter
    def current_builder(self, new_builder: AbstractCarBuilder) -> None:
        self._car_builder = new_builder

    def steady_ready_go(self, car: AbstractCar | None = None) -> None:
        if car is None:
            car = self._car_builder.create_car()
        car.drive()
