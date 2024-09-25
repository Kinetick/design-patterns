from .abc import (
    AbstractBus,
    AbstractBusVisitor,
    AbstractDevice,
    AbstractFridge,
    AbstractKettle,
    AbstractWashing,
)


class BaseKettle(AbstractKettle):
    """Базовый класс чайника."""

    def __init__(
        self,
        width: int,
        length: int,
        height: int,
        model: str,
        max_water_volume: float,
    ) -> None:
        self._dimensions = (length, width, height)
        self._model = model
        self._max_water_volume = max_water_volume
        self._current_water_volume = 0

    @property
    def max_water_volume(self) -> float:
        return self._max_water_volume

    @property
    def current_water_volume(self) -> float:
        return self._current_water_volume

    @current_water_volume.setter
    def current_water_volume(self, water: float) -> None:
        water_constraint = 0 <= water <= self._max_water_volume
        self._current_water_volume = (
            water if water_constraint else self._max_water_volume
        )

    @property
    def model(self) -> str:
        return self._model

    @property
    def dimensions(self) -> tuple[int, int, int]:
        return self._dimensions

    def accept(self, visitor: AbstractBusVisitor) -> None:
        visitor.visit_kettle(self)


class BaseFridge(AbstractFridge):
    def __init__(
        self,
        width: int,
        length: int,
        height: int,
        model: str,
        non_freezer_min_degrees: int,
        freezer_min_degrees: int,
        chambers_count: int,
    ) -> None:

        self._dimensions = (length, width, height)
        self._model = model
        self._non_freezer_min = non_freezer_min_degrees
        self._freezer_min = freezer_min_degrees
        self._chambers_count = chambers_count
        self._current_degrees = (0, 0)

    @property
    def chambers_count(self) -> int:
        return self._chambers_count

    @property
    def non_freezer_min_degrees(self) -> int:
        return self._non_freezer_min

    @property
    def freezer_min_degrees(self) -> int:
        return self._freezer_min

    @property
    def current_degrees(self) -> tuple[int, int]:
        return self._current_degrees

    @current_degrees.setter
    def current_degrees(self, degrees: tuple[int, int]) -> None:
        non_freezer_constriction = degrees[1] >= self._non_freezer_min
        freezer_constriction = degrees[0] >= self._freezer_min

        freezer_degrees = (
            degrees[0] if freezer_constriction else self._freezer_min
        )
        non_freezer_degrees = (
            degrees[1] if non_freezer_constriction else self._non_freezer_min
        )
        self._current_degrees = (freezer_degrees, non_freezer_degrees)

    @property
    def model(self) -> str:
        return self._model

    @property
    def dimensions(self) -> tuple[int, int, int]:
        return self._dimensions

    def accept(self, visitor: AbstractBusVisitor) -> None:
        visitor.visit_fridge(self)


class BaseWashing(AbstractWashing):
    def __init__(
        self,
        width: int,
        length: int,
        height: int,
        model: str,
        max_clothes_load: float,
        max_water_consumption: float,
    ) -> None:
        self._dimensions = (length, width, height)
        self._model = model
        self._max_clothes = max_clothes_load
        self._max_water = max_water_consumption
        self._current_clothes = 0

    @property
    def max_clothes_load(self) -> float:
        return self._max_clothes

    @property
    def max_water_consumption(self) -> float:
        return self._max_water

    @property
    def current_clothes_load(self) -> float:
        return self._current_clothes

    @current_clothes_load.setter
    def current_clothes_load(self, clothes: float) -> None:
        clothes_constraint = 0 <= clothes <= self._max_clothes
        self._current_clothes = (
            clothes if clothes_constraint else self._max_clothes
        )

    @property
    def model(self) -> str:
        return self._model

    @property
    def dimensions(self) -> tuple[int, int, int]:
        return self._dimensions

    def accept(self, visitor: AbstractBusVisitor) -> None:
        visitor.visit_washing(self)


class BaseBus(AbstractBus):
    """Базовый класс шины бытовых приборов."""

    def __init__(
        self, devices: dict[str, AbstractDevice] | None = None
    ) -> None:
        self._devices = devices if devices else {}

    def register_device(self, device: AbstractDevice) -> None:
        self._devices[device.model] = device

    def unregister_device(self, model: str) -> None:
        self._devices.pop(model, None)

    def accept(self, visitor: AbstractBusVisitor) -> None:
        for device in self._devices.values():
            device.accept(visitor=visitor)
