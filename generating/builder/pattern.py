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
        print(self, "Погнали - ВРУУУУУМММ!", sep="\n")


class AbstractCarBuilder(ABC):
    """Абстрактный строитель автомобиля."""

    @abstractmethod
    def build_wheels(cls) -> BaseWheels:
        """Интерфейс создания колес автомобиля."""
        ...

    @abstractmethod
    def build_engine(cls) -> BaseEngine:
        """Интерфейс создания двигателя автомобиля."""
        ...

    @abstractmethod
    def build_body(cls) -> BaseBody:
        """Интерфейс создания кузова автомобиля."""
        ...

    # * По сути, интерфейс ниже может использовать "Шаблонный метод", т.к.
    # * логика создания автомобиля всегда одна.
    @abstractmethod
    def create_car(cls) -> BaseCar:
        """Интерфейс создания автомобиля."""
        ...
