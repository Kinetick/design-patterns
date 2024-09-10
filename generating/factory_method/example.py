from .pattern import (
    AbstractEngine,
    AbstractTechnicalStation,
    BaseMechanic,
)


class DieselEngine(AbstractEngine):
    """Дизельный двигатель."""

    def start_diagnostic(self) -> bool:
        print("Запуск диагностики дизельного двигателя.")

        return self.is_broken

    def start_engine(self) -> None:
        print("Запуск дизельного двигателя.")


class GasolineEngine(AbstractEngine):
    """Бензиновый двигатель."""

    def start_diagnostic(self) -> bool:
        print("Запуск диагностики бензинового двигателя.")

        return self.is_broken

    def start_engine(self) -> None:
        print("Запуск бензинового двигателя.")


class TurboEngine(AbstractEngine):
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


class TechnicalStation1(AbstractTechnicalStation):
    """Техническая станция №1."""

    @classmethod
    def call_mechanic(cls, engine: AbstractEngine) -> BaseMechanic | None:
        """Фабричный метод вызова механика на станции №1."""

        mechanic = None
        if isinstance(engine, DieselEngine):
            mechanic = DieselMechanic(name="Коля")
        elif isinstance(engine, GasolineEngine):
            mechanic = GasolineMechanic(name="Толя")
        elif isinstance(engine, TurboEngine):
            mechanic = TurboMechanic(name="Оля")

        return mechanic
