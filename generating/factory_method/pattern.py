from abc import ABC, abstractmethod
from random import randint


class AbstractEngine(ABC):
    """Абстрактный класс двигателя."""

    def __init__(self, is_broken: bool) -> None:
        self._is_broken = is_broken

    @property
    def is_broken(self) -> bool:
        """Св-во состояния двигателя."""
        return self._is_broken

    @is_broken.setter
    def is_broken(self, new_engine_state: bool) -> None:
        self._is_broken = new_engine_state

    @abstractmethod
    def start_engine(self) -> None:
        """Интерфейс запуска двигателя."""
        ...

    def start_diagnostic(self) -> bool:
        """Интерфейс запуска диагностики двигателя."""
        ...


class BaseMechanic:
    """Класс описывающий базового автослесаря."""

    def __init__(self, name: str, service_type: str) -> None:
        self._name = name
        self._service_type = service_type

    def service_engine(self, engine: AbstractEngine) -> None:
        """Метод реализующий логику обслуживания двигателя."""
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


class AbstractTechnicalStation(ABC):
    """Абстрактная техническая станция."""

    def process_order(self, engine: AbstractEngine) -> None:
        """Логика обработки заказа на обслуживание двигателя."""
        mechanic = self.call_mechanic(engine=engine)
        mechanic.service_engine(engine=engine)

    @abstractmethod
    def call_mechanic(cls, engine: AbstractEngine) -> BaseMechanic:
        """Абстрактный фабричный метод - вызова специалиста."""
        ...
