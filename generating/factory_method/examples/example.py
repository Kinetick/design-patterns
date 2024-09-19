from ..pattern.base import (
    BaseEngine,
    BaseMechanic,
    BaseTechnicalStation,
)


class DieselEngine(BaseEngine):
    """Дизельный двигатель."""

    def start_diagnostic(self) -> bool:
        print("Запуск диагностики дизельного двигателя.")

        return self.is_broken

    def start_engine(self) -> None:
        print("Запуск дизельного двигателя.")


class GasolineEngine(BaseEngine):
    """Бензиновый двигатель."""

    def start_diagnostic(self) -> bool:
        print("Запуск диагностики бензинового двигателя.")

        return self.is_broken

    def start_engine(self) -> None:
        print("Запуск бензинового двигателя.")


class TurboEngine(BaseEngine):
    """Турбированный двигатель."""

    def start_diagnostic(self) -> bool:
        print("Запуск диагностики турбинного двигателя.")

        return self.is_broken

    def start_engine(self) -> None:
        print("Запуск турбинного двигателя.")


class DieselMechanic(BaseMechanic):
    """Чинила дизельных двигателей."""

    def __init__(self, name: str, service_type: str = "Дизель") -> None:
        super().__init__(name, service_type)


class GasolineMechanic(BaseMechanic):
    """Чинила бензиновых двигателей."""

    def __init__(self, name: str, service_type: str = "Бензин") -> None:
        super().__init__(name, service_type)


class TurboMechanic(BaseMechanic):
    """Чинила турбо двигателей."""

    def __init__(self, name: str, service_type: str = "Турбо") -> None:
        super().__init__(name, service_type)


common_technical_station = BaseTechnicalStation()
common_technical_station.register_mechanic(
    mechanic=DieselMechanic(name="Коля"), engine=DieselEngine(is_broken=True)
)
common_technical_station.register_mechanic(
    mechanic=TurboMechanic(name="Саша"), engine=DieselEngine(is_broken=True)
)
common_technical_station.register_mechanic(
    mechanic=GasolineMechanic(name="Маша"), engine=DieselEngine(is_broken=True)
)
