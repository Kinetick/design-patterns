from .abc import (
    AbstractGasolineObservable,
    AbstractGasolineObserver,
)


class BaseGasolineObserver(AbstractGasolineObserver):
    """Базовый класс наблюдателя за уровнем топлива."""

    def __init__(self, work_modes_map: dict[float, str]) -> None:
        self._modes = list(work_modes_map.items())
        self._modes.sort(key=lambda x: x[0])
        self._current_mode = None
        self._gasoline_percent = None

    @property
    def cur_mode(self) -> str | None:
        return self._current_mode

    @cur_mode.setter
    def cur_mode(self, new_mode: str | None) -> None:
        self._current_mode = new_mode
        if new_mode is not None:
            self._current_mode = str(new_mode)

    def find_nearest_mode(
        self, gasoline_percent: float | None
    ) -> tuple[float, str] | None:
        result = None
        searchable_modes = self._modes

        while gasoline_percent and searchable_modes and result is None:
            count_modes = len(searchable_modes)
            if count_modes == 1:
                result = searchable_modes[0]
            elif count_modes == 2:
                result = searchable_modes[0]
                if searchable_modes[0][0] < gasoline_percent:
                    result = searchable_modes[1]

            middle_index = (count_modes - 1) // 2
            middle_mode = searchable_modes[middle_index]
            if middle_mode[0] < gasoline_percent:
                searchable_modes = searchable_modes[middle_index + 1 :]
            else:
                searchable_modes = searchable_modes[: middle_index + 1]

        return result

    def update(self, gasoline_percent: float) -> None:
        new_mode = self.find_nearest_mode(gasoline_percent)
        self.cur_mode = new_mode[1] if new_mode else new_mode
        print(self)

    def __str__(self) -> str:
        """Отображение состояния устройства."""
        description = f"""
            Тип устройства: {self.__class__.__name__}
            Текущий режим работы: {self._current_mode}
        """

        return description


class BaseGasolineObservable(AbstractGasolineObservable):
    """Базовый наблюдаемы за уровнем топлива."""

    def __init__(
        self,
        observers: dict[str, AbstractGasolineObserver] | None = None,
        gasoline_level: float | None = None,
    ) -> None:
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

    def update_gasoline_level(self, gasoline_level: float) -> None:
        self._gasoline_level = gasoline_level
        self.notify_observers()

    def notify_observers(self) -> None:
        if self._gasoline_level is not None:
            for observer in self._observes.values():
                observer.update(self._gasoline_level)
