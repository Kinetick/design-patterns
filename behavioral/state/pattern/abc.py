from abc import ABC, abstractmethod


class AbstractEngine(ABC):
    """Описание интерфейса двигателя."""

    @property
    @abstractmethod
    def temperature_state(self) -> "AbstractTemperatureState":
        """Температурное состояние двигателя."""
        ...

    @temperature_state.setter
    @abstractmethod
    def temperature_state(self, new_state: "AbstractTemperatureState") -> None:
        """Температурное состояние двигателя."""
        ...

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

    @abstractmethod
    def prepare_fillers(self) -> dict[str, str | bool]:
        """Интерфейс подготовки заполнителей для эхо."""
        ...

    @abstractmethod
    def echo_state(self) -> None:
        """Интерфейс печати текущего состояния."""
        ...

    def set_prev(self, state: "AbstractTemperatureState") -> None:
        """Интерфейс назначения предыдущего состояния."""
        ...

    def set_next(self, state: "AbstractTemperatureState") -> None:
        """Интерфейс назначения следующего состояния."""
        ...

    def increase_rpm(self, engine: AbstractEngine) -> None:
        """Интерфейс увеличения числа оборотов."""
        ...

    def decrease_rpm(self, engine: AbstractEngine) -> None:
        """Интерфейс уменьшения числа оборотов."""
        ...
