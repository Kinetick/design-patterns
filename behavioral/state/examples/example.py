from ..pattern.base import BaseEngine, BaseTemperatureState


class ColdStartState(BaseTemperatureState):
    """Состояние холодного пуска."""

    def prepare_fillers(self) -> dict[str, bool | str]:
        return {
            "class_name": self.__class__.__name__,
            "cooling_system": False,
            "allow_increase_rpm": True,
            "allow_decrease_rpm": False,
        }


class HotStartState(BaseTemperatureState):
    """Состояние горячего запуска."""

    def prepare_fillers(self) -> dict[str, bool | str]:
        return {
            "class_name": self.__class__.__name__,
            "cooling_system": False,
            "allow_increase_rpm": True,
            "allow_decrease_rpm": True,
        }


class HighTemperatureState(BaseTemperatureState):
    """Состояние повышенной температуры."""

    def prepare_fillers(self) -> dict[str, bool | str]:
        return {
            "class_name": self.__class__.__name__,
            "cooling_system": True,
            "allow_increase_rpm": True,
            "allow_decrease_rpm": True,
        }


class ExtremeTemperatureState(BaseTemperatureState):
    """Состояние экстремальной температуры."""

    def prepare_fillers(self) -> dict[str, bool | str]:
        return {
            "class_name": self.__class__.__name__,
            "cooling_system": True,
            "allow_increase_rpm": False,
            "allow_decrease_rpm": True,
        }


cold_state = ColdStartState()
hot_state = HotStartState()
hight_state = HighTemperatureState()
extreme_state = ExtremeTemperatureState()

hot_state.set_prev(cold_state)
hot_state.set_next(hight_state)
hight_state.set_prev(hot_state)
hight_state.set_next(extreme_state)
extreme_state.set_prev(hight_state)

common_engine = BaseEngine(temperature_state=cold_state)
