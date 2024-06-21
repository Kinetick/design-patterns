from abc import ABC, abstractmethod


class AbstractEngine(ABC):
    """Описание интерфейса двигателя."""

    def __init__(self, temperature_state: "AbstractTemperatureState") -> None:
        self.temperature_state = temperature_state

    @abstractmethod
    def increase_rpm(self) -> None:
        """Интерфейс увеличения оборотов двигателя."""
        ...

    @abstractmethod
    def decrease_rpm(self) -> None:
        """Интерфейс уменьшения оборотов двигателя."""
        ...


class AbstractTemperatureState(ABC):
    """Описание интерфейса температурного состояния."""

    _ECHO_TEMPLATE = """
            Текущее состояние: {class_name}
            Система охлаждения: {cooling_system}
            Допустимость повышения оборотов: {allow_increase_rpm}
            Допустимость снижения оборотов: {allow_decrease_rpm}
        """

    def __init__(
        self,
        prev_state: "AbstractTemperatureState | None" = None,
        next_state: "AbstractTemperatureState | None" = None,
    ) -> None:
        self._prev_state = prev_state
        self._next_state = next_state

    @abstractmethod
    def echo_state(self) -> None:
        """Интерфейс печати текущего состояния."""
        ...

    def set_prev(self, state: "AbstractTemperatureState") -> None:
        """Интерфейс назначения предыдущего состояния."""
        self._prev_state = state

    def set_next(self, state: "AbstractTemperatureState") -> None:
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
