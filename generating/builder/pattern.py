

from abc import ABC, abstractmethod


class BaseEngine:
    """Базовый класс двигателя."""

    def __init__(self, gas_type: str) -> None:
        self._gas_type = gas_type

    def __str__(self) -> str:
        description = f"""
            Тип топлива: {self._gas_type}
        """

        return description


class BaseWheels:
    """Базовый класс колес."""

    def __init__(self, diameter: int) -> None:
        self._diameter = diameter

    def __str__(self) -> str:
        description = f"""
            Диаметр колес, см: {self._diameter}
        """

        return description


class BaseBody:
    """Базовый класс кузова."""

    def __init__(self, body_type: str) -> None:
        self._body_type = body_type

    def __str__(self) -> str:
        description = f"""
            Тип кузова: {self._body_type}
        """

        return description


class BaseCar:
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
        print(self, 'Погнали - ВРУУУУУМММ!', sep='\n')


class AbstractCarBuilder(ABC):
    """Абстрактный строитель автомобиля."""

    @abstractmethod
    def build_wheels(cls) -> BaseWheels:
        ...

    @abstractmethod
    def build_engine(cls) -> BaseEngine:
        ...

    @abstractmethod
    def build_body(cls) -> BaseBody:
        ...

    @abstractmethod
    def create_car(cls) -> BaseCar:
        ...


class DieselCarBuilder(AbstractCarBuilder):
    """Строитель дизельного автомобиля"""

    @classmethod
    def build_engine(cls) -> BaseEngine:
        """Фабричный метод дизельного двигателя."""

        return BaseEngine(gas_type='Diesel')

    @classmethod
    def build_wheels(cls) -> BaseWheels:
        """Фабричный метод колес дизельного автомобиля."""

        return BaseWheels(diameter=22)

    @classmethod
    def build_body(cls) -> BaseBody:
        """Фабричный метод кузова дизельного двигателя."""

        return BaseBody(body_type='Jeep')

    def create_car(self) -> BaseCar:
        """Фабричный метод создания дизельного автомобиля."""

        return BaseCar(
            body=self.build_body(),
            engine=self.build_engine(),
            wheels=self.build_wheels()
        )
