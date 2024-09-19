from .abc import AbstractEngine, AbstractTemperatureState


class BaseTemperatureState(AbstractTemperatureState):
    """Базовый класс температурного состояния."""

    _ECHO_TEMPLATE = """
            Текущее состояние: {class_name}
            Система охлаждения: {cooling_system}
            Допустимость повышения оборотов: {allow_increase_rpm}
            Допустимость снижения оборотов: {allow_decrease_rpm}
        """

    def __init__(
        self,
        prev_state: AbstractTemperatureState | None = None,
        next_state: AbstractTemperatureState | None = None,
    ) -> None:
        self._prev_state = prev_state
        self._next_state = next_state

    def echo_state(self) -> None:
        print(self._ECHO_TEMPLATE.format(**self.prepare_fillers()))

    def set_prev(self, state: AbstractTemperatureState) -> None:
        """Интерфейс назначения предыдущего состояния."""
        self._prev_state = state

    def set_next(self, state: AbstractTemperatureState) -> None:
        """Интерфейс назначения следующего состояния."""
        self._next_state = state

    def increase_rpm(self, engine: AbstractEngine) -> None:
        """Интерфейс увеличения числа оборотов."""
        self.echo_state()
        if self._next_state:
            engine.temperature_state = self._next_state
        else:
            engine.temperature_state = self

    def decrease_rpm(self, engine: AbstractEngine) -> None:
        """Интерфейс уменьшения числа оборотов."""
        self.echo_state()
        if self._prev_state:
            engine.temperature_state = self._prev_state
        else:
            engine.temperature_state = self


class BaseEngine(AbstractEngine):
    """Базовый класс двигателя."""

    def __init__(self, temperature_state: "AbstractTemperatureState") -> None:
        self._temperature_state = temperature_state

    @property
    def temperature_state(self) -> AbstractTemperatureState:
        return self._temperature_state

    @temperature_state.setter
    def temperature_state(self, new_state: AbstractTemperatureState) -> None:
        self._temperature_state = new_state

    def increase_rpm(self) -> None:
        self._temperature_state.increase_rpm(self)

    def decrease_rpm(self) -> None:
        self._temperature_state.decrease_rpm(self)
