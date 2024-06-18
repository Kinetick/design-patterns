from abc import ABC, abstractmethod


class BaseEngine:
    """Базовый класс - двигателя."""

    def __init__(self, is_broken: bool) -> None:
        self._is_broken = is_broken

    def start_engine(self) -> None:
        """Запуск дизельного двигателя."""
        print(self.start_engine.__doc__)

    def start_diagnostic(self) -> bool:
        """Запуск диагностики дизельного двигателя."""
        print(self.start_diagnostic.__doc__)

        return self._is_broken


class BaseMechanic:
    """Класс описывающий базового автослесаря."""

    def __init__(self, name: str, service_type: str) -> None:
        self._name = name
        self._service_type = service_type

    @abstractmethod
    def service_engine(self, engine: BaseEngine) -> None:
        """Метод реализующий логику обслуживания двигателя."""
        service_message = f"""
            Имя специалиста: {self._name}
            Тип обслуживаемого двигателя: {self._service_type}
            Класс обслуживаемого двигателя: {engine.__class__.__name__}
        """
        print(service_message)
        is_broken = engine.start_diagnostic()
        if is_broken:
            engine._is_broken = False
        engine.start_engine()


class AbstractTechnicalStation(ABC):
    """Абстрактная техническая станция."""

    def process_order(self, engine: BaseEngine) -> None:
        """Логика обработки заказа на обслуживание двигателя."""
        mechanic = self.call_mechanic(engine=engine)
        mechanic.service_engine(engine=engine)

    @abstractmethod
    def call_mechanic(cls, engine: BaseEngine) -> BaseMechanic:
        """Абстрактный фабричный метод - вызова специалиста."""
        ...
