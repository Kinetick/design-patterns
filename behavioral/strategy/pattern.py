from abc import ABC, abstractmethod


class AbstractGear(ABC):
    """Интерфейс скорости автомобиля."""

    @abstractmethod
    def change_movement(self) -> str:
        """Интерфейс смены состояния движения автомобиля."""
        raise NotImplementedError

    def __str__(self) -> str:
        return self.__class__.__name__


class BaseCar:
    """Базовый класс автомобиля."""

    def __init__(self, gear: AbstractGear) -> None:
        self._current_gear = gear
        self._movement_state = None

    def set_gear(self, gear: AbstractGear) -> None:
        """Интерфейс переключения скоростей."""
        self._current_gear = gear

    def move(self) -> None:
        """Интерфейс движения вперед."""
        self._movement_state = self._current_gear.change_movement()
        print(self)

    def __str__(self) -> str:
        """Описание текущего состояния автомобиля."""
        description = f"""
            Тип автомобиля: {self.__class__.__name__}
            Текущая передача: {self._current_gear}
            Текущее движение: {self._movement_state}
        """

        return description
