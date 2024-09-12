from typing import Any

from .pattern import BaseEngine, BaseTemperatureState


class ColdStartState(BaseTemperatureState):
    """Состояние холодного пуска."""

    def prepare_fillers(self) -> dict[str, Any]:
        return {
            "class_name": self.__class__.__name__,
            "cooling_system": False,
            "allow_increase_rpm": True,
            "allow_decrease_rpm": False,
        }


class HotStartState(BaseTemperatureState):
    """Состояние горячего запуска."""

    def prepare_fillers(self) -> dict[str, Any]:
        return {
            "class_name": self.__class__.__name__,
            "cooling_system": False,
            "allow_increase_rpm": True,
            "allow_decrease_rpm": True,
        }


class HighTemperatureState(BaseTemperatureState):
    """Состояние повышенной температуры."""

    def prepare_fillers(self) -> dict[str, Any]:
        return {
            "class_name": self.__class__.__name__,
            "cooling_system": True,
            "allow_increase_rpm": True,
            "allow_decrease_rpm": True,
        }


class ExtremeTemperatureState(BaseTemperatureState):
    """Состояние экстремальной температуры."""

    def prepare_fillers(self) -> dict[str, Any]:
        return {
            "class_name": self.__class__.__name__,
            "cooling_system": True,
            "allow_increase_rpm": False,
            "allow_decrease_rpm": True,
        }


class GasolineEngine(BaseEngine):
    """Двигатель внутреннего сгорания."""
