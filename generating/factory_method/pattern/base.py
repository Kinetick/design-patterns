from random import randint

from .abc import (
    AbstractEngine,
    AbstractMechanic,
    AbstractTechnicalStation,
)


class BaseEngine(AbstractEngine):
    """Базовый класс двигателя."""

    def __init__(self, is_broken: bool) -> None:
        self._is_broken = is_broken

    @property
    def is_broken(self) -> bool:
        """Св-во состояния двигателя."""
        return self._is_broken

    @is_broken.setter
    def is_broken(self, new_engine_state: bool) -> None:
        self._is_broken = new_engine_state


class BaseMechanic(AbstractMechanic):
    """Базовый класс механика."""

    def __init__(self, name: str, service_type: str) -> None:
        self._name = name
        self._service_type = service_type

    def service_engine(self, engine: AbstractEngine) -> None:
        print(
            f"""
                Имя специалиста: {self._name}
                Тип обслуживаемого двигателя: {self._service_type}
                Класс обслуживаемого двигателя: {engine.__class__.__name__}
            """
        )

        while not engine.start_diagnostic():
            print("Двигатель не исправен, начинаю ремонт.")
            engine.is_broken = bool(randint(0, 1))

        engine.start_engine()


class BaseTechnicalStation(AbstractTechnicalStation):

    def __init__(
        self,
        mechanics_map: dict[AbstractEngine, AbstractMechanic] | None = None,
    ) -> None:
        self._mechanics_map = mechanics_map if mechanics_map else {}

    def process_order(self, engine: AbstractEngine) -> None:
        mechanic = self.call_mechanic(engine=engine)
        if mechanic is None:
            print(f"Механик для двигателя: {engine} не найден.")
            return None

        mechanic.service_engine(engine=engine)

    def register_mechanic(
        self, mechanic: AbstractMechanic, engine: AbstractEngine
    ) -> None:
        self._mechanics_map[engine] = mechanic

    def call_mechanic(self, engine: AbstractEngine) -> AbstractMechanic | None:

        return self._mechanics_map.get(engine)
