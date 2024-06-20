from .pattern import AbstractGear, BaseCar


class WarTrackCar(BaseCar):
    """Автомобиль орков из Warhammer 40k."""

    ...


class FirstGear(AbstractGear):
    """Первая передача."""

    def change_movement(self) -> str:
        return "Слегка вперед."


class SecondGear(AbstractGear):
    """Вторая передача."""

    def change_movement(self) -> str:
        return "Очень вперед."


class LastGear(AbstractGear):
    """Последняя передача."""

    def change_movement(self) -> str:
        return "WAAAAAGH!!!"


class NeutralGear(AbstractGear):
    """Нейтральная передача."""

    def change_movement(self) -> str:
        return "Ни вперед, ни назад."


class ReverseGear(AbstractGear):
    """Задняя передача."""

    def change_movement(self) -> str:
        return "Не вперед, а назад."
