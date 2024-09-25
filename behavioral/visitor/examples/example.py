from behavioral.visitor.pattern.abc import (
    AbstractFridge,
    AbstractKettle,
    AbstractWashing,
)

from ..pattern.abc import AbstractBusVisitor
from ..pattern.base import (
    BaseBus,
    BaseFridge,
    BaseKettle,
    BaseWashing,
)


class CurrentVisiter(AbstractBusVisitor):
    def visit_fridge(self, fridge: AbstractFridge) -> None:
        current_message = f"""
            Модель холодильника: {fridge.model}
            Текущая температура морозилки: {fridge.current_degrees[0]}
            Текущая температура камер: {fridge.current_degrees[1]}
        """
        print(current_message)

    def visit_kettle(self, kettle: AbstractKettle) -> None:
        current_message = f"""
            Модель чайника: {kettle.model}
            Текущий объем воды: {kettle.current_water_volume}
        """
        print(current_message)

    def visit_washing(self, washing: AbstractWashing) -> None:
        current_message = f"""
            Модель стиральной машины: {washing.model}
            Текущая загрузка белья: {washing.current_clothes_load}
        """
        print(current_message)


class AmericanVisitor(AbstractBusVisitor):
    INCH_COEFFICIENT = 2.54
    GALLON_COEFFICIENT = 4.546
    FAHRENHEIT_COEFFICIENT = 32
    FOUNT_COEFFICIENT = 2.2

    def visit_fridge(self, fridge: AbstractFridge) -> None:
        min_non_freezer = (
            fridge.non_freezer_min_degrees * self.FAHRENHEIT_COEFFICIENT
        )
        min_freezer = fridge.freezer_min_degrees * self.FAHRENHEIT_COEFFICIENT

        fridge_info = f"""
            Модель холодильника: {fridge.model}
            Высота, дюймов: {fridge.dimensions[2] * self.INCH_COEFFICIENT}
            Ширина, дюймов: {fridge.dimensions[1] * self.INCH_COEFFICIENT}
            Длина, дюймов: {fridge.dimensions[0] * self.INCH_COEFFICIENT}
            Минимальная температура камер, F {min_non_freezer}
            Минимальная температура морозилки, F {min_freezer}
            Кол-во камер: {fridge.chambers_count}
        """
        print(fridge_info)

    def visit_kettle(self, kettle: AbstractKettle) -> None:
        max_water = kettle.max_water_volume * self.GALLON_COEFFICIENT

        kettle_info = f"""
            Модель чайника: {kettle.model}
            Высота, дюймов {kettle.dimensions[2] * self.INCH_COEFFICIENT}
            Ширина, дюймов {kettle.dimensions[1] * self.INCH_COEFFICIENT}
            Длина, дюймов {kettle.dimensions[0] * self.INCH_COEFFICIENT}
            Максимальный объем воды, галлонов {max_water}
        """
        print(kettle_info)

    def visit_washing(self, washing: AbstractWashing) -> None:
        max_load = washing.max_clothes_load * self.FOUNT_COEFFICIENT
        max_water = washing.max_water_consumption * self.GALLON_COEFFICIENT

        washing_info = f"""
            Модель стиральной машины: {washing.model}
            Высота, дюймов {washing.dimensions[2] * self.INCH_COEFFICIENT}
            Ширина, дюймов {washing.dimensions[1] * self.INCH_COEFFICIENT}
            Длина, дюймов {washing.dimensions[0] * self.INCH_COEFFICIENT}
            Максимальная загрузка белья, фунтов {max_load}
            Максимальный расход воды, галлонов {max_water}
        """
        print(washing_info)


class MetricVisiter(AbstractBusVisitor):
    def visit_fridge(self, fridge: AbstractFridge) -> None:
        fridge_info = f"""
            Модель холодильника: {fridge.model}
            Высота, см: {fridge.dimensions[2]}
            Ширина, см: {fridge.dimensions[1]}
            Длина, см: {fridge.dimensions[0]}
            Минимальная температура камер, C {fridge.non_freezer_min_degrees}
            Минимальная температура морозилки, С {fridge.freezer_min_degrees}
            Кол-во камер: {fridge.chambers_count}
        """
        print(fridge_info)

    def visit_kettle(self, kettle: AbstractKettle) -> None:
        kettle_info = f"""
            Модель чайника: {kettle.model}
            Высота, см {kettle.dimensions[2]}
            Ширина, см {kettle.dimensions[1]}
            Длина, см {kettle.dimensions[0]}
            Максимальный объем воды, л {kettle.max_water_volume}
        """
        print(kettle_info)

    def visit_washing(self, washing: AbstractWashing) -> None:
        washing_info = f"""
            Модель стиральной машины: {washing.model}
            Высота, см {washing.dimensions[2]}
            Ширина, см {washing.dimensions[1]}
            Длина, см {washing.dimensions[0]}
            Максимальная загрузка белья, кг {washing.max_clothes_load}
            Максимальный расход воды, л {washing.max_water_consumption}
        """
        print(washing_info)


current_visiter = CurrentVisiter()
american_visitor = AmericanVisitor()
metric_visitor = MetricVisiter()
samsung_kettle = BaseKettle(
    width=15,
    length=20,
    height=30,
    model="TEST_KETTLE",
    max_water_volume=2,
)
stinol_fridge = BaseFridge(
    width=40,
    length=40,
    height=170,
    model="TEST_STINOL",
    non_freezer_min_degrees=-10,
    freezer_min_degrees=-15,
    chambers_count=3,
)
lg_washing = BaseWashing(
    width=35,
    length=50,
    height=100,
    model="TEST_LG",
    max_clothes_load=5,
    max_water_consumption=10,
)

common_bus = BaseBus()
common_bus.register_device(samsung_kettle)
common_bus.register_device(lg_washing)
common_bus.register_device(stinol_fridge)
