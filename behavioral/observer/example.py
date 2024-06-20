from .pattern import (
    AbstractGasolineObservable,
    AbstractGasolineObserver,
)


class InjectionProcessor(AbstractGasolineObserver):
    """Процессор впрыска топлива в двигатель."""

    def __init__(
        self, injection_mode: str = "default", economy_floor: float = 0.35
    ) -> None:
        super().__init__()
        self._injection_mode = injection_mode
        self._economy_floor = economy_floor

    def update(self, gasoline_percent: float | None) -> None:
        if (
            gasoline_percent is not None
            and gasoline_percent < self._economy_floor
        ):
            self._injection_mode = "economy"
        print(self)

    def __str__(self) -> str:
        """Отображение состояния устройства."""
        description = f"""
            Тип устройства: {self.__class__.__name__}
            Текущий режим работы: {self._injection_mode}
        """

        return description


class MicroclimateProcessor(AbstractGasolineObserver):
    """Процессор микроклимата в салоне."""

    def __init__(
        self, microclimate_mode: str = "on", economy_floor: float = 0.50
    ) -> None:
        super().__init__()
        self._microclimate_mode = microclimate_mode
        self._economy_floor = economy_floor

    def update(self, gasoline_percent: float | None) -> None:
        if (
            gasoline_percent is not None
            and gasoline_percent < self._economy_floor
        ):
            self._microclimate_mode = "off"
        print(self)

    def __str__(self) -> str:
        """Отображение состояния устройства."""
        description = f"""
            Тип устройства: {self.__class__.__name__}
            Состояние кондиционера: {self._microclimate_mode}
        """

        return description


class GasolineDisplay(AbstractGasolineObserver):
    """Дисплей уровня топлива."""

    def __init__(
        self, alert_mode: bool = False, alert_floor: float = 0.2
    ) -> None:
        super().__init__()
        self._alert_mode = alert_mode
        self._alert_floor = alert_floor
        self._gasoline_level = None

    def update(self, gasoline_percent: float | None) -> None:
        if (
            gasoline_percent is not None
            and gasoline_percent < self._alert_floor
        ):
            self._alert_mode = True
        self._gasoline_level = gasoline_percent
        print(self)

    def __str__(self) -> str:
        """Отображение информации об уровне топлива."""
        description = f"""
            Текущий уровень топлива: {self._gasoline_level}
            Слишком низкий уровень топлива: {self._alert_mode}
        """

        return description


class GasolineLevelSensor(AbstractGasolineObservable):
    """Датчик уровня топлива."""

    def __init__(
        self,
        observers: dict[str, AbstractGasolineObserver] | None = None,
        gasoline_level: float | None = None,
    ) -> None:
        super().__init__()
        self._observes = observers or {}
        self._gasoline_level = gasoline_level

    def register_observer(self, observer: AbstractGasolineObserver) -> None:
        self._observes[observer.__class__.__name__] = observer

    def unregister_observer(
        self, observer: AbstractGasolineObserver | str
    ) -> AbstractGasolineObserver | None:
        observer_key = observer.__class__.__name__
        if isinstance(observer, str):
            observer_key = observer

        unregistered_observer = self._observes.pop(observer_key, None)

        return unregistered_observer

    def receive_gasoline_level(self, gasoline_level: float) -> None:
        self._gasoline_level = gasoline_level
        self.notify_observers()

    def notify_observers(self) -> None:
        if self._gasoline_level is not None:
            for observer in self._observes.values():
                observer.update(self._gasoline_level)
