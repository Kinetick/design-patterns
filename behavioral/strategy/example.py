from .pattern import BaseCar, BaseGear


class WarTrackCar(BaseCar):
    """Автомобиль орков из Warhammer 40k."""

    ...


class FirstGear(BaseGear):
    """Первая передача."""

    def change_movement(self) -> str:
        return "Слегка вперед."


class SecondGear(BaseGear):
    """Вторая передача."""

    def change_movement(self) -> str:
        return "Очень вперед."


class LastGear(BaseGear):
    """Последняя передача."""

    def change_movement(self) -> str:
        return "WAAAAAGH!!!"


class NeutralGear(BaseGear):
    """Нейтральная передача."""

    def change_movement(self) -> str:
        return "Ни вперед, ни назад."


class ReverseGear(BaseGear):
    """Задняя передача."""

    def change_movement(self) -> str:
        return "Не вперед, а назад."
