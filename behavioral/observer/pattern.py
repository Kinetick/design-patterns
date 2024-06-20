from abc import ABC, abstractmethod


class AbstractGasolineObserver(ABC):
    """Абстрактный наблюдатель за уровнем топлива."""

    @abstractmethod
    def update(self, gasoline_percent: float) -> None:
        """Интерфейс обновления состояния наблюдателя."""
        raise NotImplementedError


class AbstractGasolineObservable(ABC):
    """Абстрактный наблюдаемы за топливом набор интерфейсов."""

    @abstractmethod
    def register_observer(self, observer: AbstractGasolineObserver) -> None:
        """Интерфейс регистрации наблюдателя за уровнем топлива."""
        raise NotImplementedError

    @abstractmethod
    def unregister_observer(
        self, observer: AbstractGasolineObserver | str
    ) -> AbstractGasolineObserver | None:
        """Интерфейс исключения наблюдателя."""
        raise NotImplementedError

    @abstractmethod
    def receive_gasoline_level(self, gasoline_level: float) -> None:
        """Интерфейс получения уровня топлива."""
        raise NotImplementedError

    @abstractmethod
    def notify_observers(self) -> None:
        """Интерфейс оповещения наблюдателей об изменения состояния."""
        raise NotImplementedError
