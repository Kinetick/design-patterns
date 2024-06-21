from .pattern import (
    AbstractEngine,
    AbstractTemperatureState,
)


class ColdStartState(AbstractTemperatureState):
    """Состояние холодного пуска."""

    def echo_state(self) -> None:
        fillers = {
            "class_name": self.__class__.__name__,
            "cooling_system": False,
            "allow_increase_rpm": True,
            "allow_decrease_rpm": False,
        }

        print(self._ECHO_TEMPLATE.format(**fillers))


class HotStartState(AbstractTemperatureState):
    """Состояние горячего запуска."""

    def echo_state(self) -> None:
        fillers = {
            "class_name": self.__class__.__name__,
            "cooling_system": False,
            "allow_increase_rpm": True,
            "allow_decrease_rpm": True,
        }

        print(self._ECHO_TEMPLATE.format(**fillers))


class HighTemperatureState(AbstractTemperatureState):
    """Состояние повышенной температуры."""

    def echo_state(self) -> None:
        fillers = {
            "class_name": self.__class__.__name__,
            "cooling_system": True,
            "allow_increase_rpm": True,
            "allow_decrease_rpm": True,
        }

        print(self._ECHO_TEMPLATE.format(**fillers))


class ExtremeTemperatureState(AbstractTemperatureState):
    """Состояние экстремальной температуры."""

    def echo_state(self) -> None:
        fillers = {
            "class_name": self.__class__.__name__,
            "cooling_system": True,
            "allow_increase_rpm": False,
            "allow_decrease_rpm": True,
        }

        print(self._ECHO_TEMPLATE.format(**fillers))


class GasolineEngine(AbstractEngine):
    """Двигатель внутреннего сгорания."""

    def increase_rpm(self) -> None:
        self.temperature_state.increase_rpm(self)

    def decrease_rpm(self) -> None:
        self.temperature_state.decrease_rpm(self)
