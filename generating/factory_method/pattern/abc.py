from abc import ABC, abstractmethod


class AbstractEngine(ABC):
    """Абстрактный класс двигателя."""

    @property
    @abstractmethod
    def is_broken(self) -> bool:
        """Св-во состояния двигателя."""
        ...

    @is_broken.setter
    @abstractmethod
    def is_broken(self, new_engine_state: bool) -> None:
        """Св-во состояния двигателя."""
        ...

    @abstractmethod
    def start_engine(self) -> None:
        """Интерфейс запуска двигателя."""
        ...

    def start_diagnostic(self) -> bool:
        """Интерфейс запуска диагностики двигателя."""
        ...


class AbstractMechanic(ABC):
    """Абстрактный класс механика."""

    @abstractmethod
    def service_engine(self, engine: AbstractEngine) -> None:
        """Интерфейс обслуживания двигателя."""
        ...


class AbstractTechnicalStation(ABC):
    """Абстрактная класс технической станции."""

    @abstractmethod
    def process_order(self, engine: AbstractEngine) -> None:
        """Интерфейс обработки заказа на обслуживание."""
        ...

    @abstractmethod
    def register_mechanic(
        self, mechanic: AbstractMechanic, engine: AbstractEngine
    ) -> None:
        """Интерфейс регистрации механика на станции."""
        ...

    @abstractmethod
    def call_mechanic(
        self, engine: AbstractEngine
    ) -> "AbstractMechanic | None":
        """Интерфейс вызова нужного механика."""
        ...
