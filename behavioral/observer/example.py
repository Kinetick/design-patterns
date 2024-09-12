from .pattern import (
    BaseGasolineObservable,
    BaseGasolineObserver,
)


class InjectionProcessor(BaseGasolineObserver):
    """Процессор впрыска топлива в двигатель."""


class MicroclimateProcessor(BaseGasolineObserver):
    """Процессор микроклимата в салоне."""


class GasolineDisplay(BaseGasolineObserver):
    """Дисплей уровня топлива."""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._current_gasoline_percent = None

    @property
    def gas_current(self) -> float | None:
        """Текущий уровень топлива."""
        return self._current_gasoline_percent

    @gas_current.setter
    def gas_current(self, new_gas_percent: float | None) -> None:
        self._current_gasoline_percent = new_gas_percent
        if new_gas_percent is not None:
            self._current_gasoline_percent = float(new_gas_percent)

    def update(self, gasoline_percent: float | None) -> None:
        self.gas_current = gasoline_percent
        new_mode = self.find_nearest_mode(gasoline_percent)
        self.cur_mode = new_mode[1] if new_mode else new_mode
        print(self)

    def __str__(self) -> str:
        """Отображение информации об уровне топлива."""
        description = f"""
            Текущий уровень топлива: {self.gas_current}
            Рабочий режим: {self.cur_mode}
        """

        return description


class GasolineLevelSensor(BaseGasolineObservable):
    """Датчик уровня топлива."""
