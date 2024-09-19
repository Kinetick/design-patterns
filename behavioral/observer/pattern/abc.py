from abc import ABC, abstractmethod


class AbstractGasolineObserver(ABC):
    """Абстрактный наблюдатель за уровнем топлива."""

    @property
    @abstractmethod
    def cur_mode(self) -> str | None:
        """Текущий режим работы."""
        ...

    @cur_mode.setter
    @abstractmethod
    def cur_mode(self, new_mode: str | None) -> None:
        """Текущий режим работы."""
        ...

    @abstractmethod
    def find_nearest_mode(
        self, gasoline_percent: float | None
    ) -> tuple[float, str] | None:
        """Интерфейс поиска ближайшего рабочего мода по уровню топлива."""
        ...

    @abstractmethod
    def update(self, gasoline_percent: float) -> None:
        """Интерфейс обновления состояния наблюдателя."""
        ...


class AbstractGasolineObservable(ABC):
    """Абстрактный наблюдаемый за топливом набор интерфейсов."""

    @abstractmethod
    def register_observer(self, observer: AbstractGasolineObserver) -> None:
        """Интерфейс регистрации наблюдателя за уровнем топлива."""
        ...

    @abstractmethod
    def unregister_observer(
        self, observer: AbstractGasolineObserver | str
    ) -> AbstractGasolineObserver | None:
        """Интерфейс исключения наблюдателя."""
        ...

    @abstractmethod
    def update_gasoline_level(self, gasoline_level: float) -> None:
        """Интерфейс получения уровня топлива."""
        ...

    @abstractmethod
    def notify_observers(self) -> None:
        """Интерфейс оповещения наблюдателей об изменения состояния."""
        ...
