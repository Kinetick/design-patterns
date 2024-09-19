from ..pattern.abc import AbstractCarBuilder
from ..pattern.base import (
    BaseBody,
    BaseCar,
    BaseCarBuilder,
    BaseDriver,
    BaseEngine,
    BaseWheels,
)


class DieselEngine(BaseEngine):
    """Дизельный двигатель."""

    def __init__(self, gas_type: str = "diesel") -> None:
        super().__init__(gas_type)


class JeepBody(BaseBody):
    """Кузов внедорожника."""

    def __init__(self, body_type: str = "jeep") -> None:
        super().__init__(body_type)


class DieselJeepBuilder(AbstractCarBuilder):
    """Пример строителя дизельного внедорожника."""

    @classmethod
    def build_engine(cls) -> BaseEngine:
        return DieselEngine()

    @classmethod
    def build_wheels(cls) -> BaseWheels:
        return BaseWheels()

    @classmethod
    def build_body(cls) -> BaseBody:
        return JeepBody()

    def create_car(self) -> BaseCar:
        return BaseCar(
            body=self.build_body(),
            engine=self.build_engine(),
            wheels=self.build_wheels(),
        )


common_driver = BaseDriver(car_builder=BaseCarBuilder())
common_driver.current_builder = DieselJeepBuilder()
