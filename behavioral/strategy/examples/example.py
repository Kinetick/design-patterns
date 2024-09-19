from ..pattern.base import BaseCar, BaseGear


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


neutral_gear = NeutralGear()
first_gear = FirstGear()
second_gear = SecondGear()
last_gear = LastGear()
reverse_gear = ReverseGear()

wartrack = BaseCar(gear=neutral_gear)
wartrack.set_gear(new_gear=first_gear)
