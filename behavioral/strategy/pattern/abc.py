from abc import ABC, abstractmethod


class AbstractGear(ABC):
    """Описание интерфейса передачи автомобиля.."""

    @abstractmethod
    def change_movement(self) -> str:
        """Интерфейс смены состояния движения автомобиля."""
        ...


class AbstractCar(ABC):
    """Описание интерфейса автомобиля."""

    @abstractmethod
    def set_gear(self, new_gear: AbstractGear) -> None:
        """Интерфейс переключения передачи."""
        ...

    @abstractmethod
    def move(self) -> None:
        """Интерфейс инициации движения."""
        ...
