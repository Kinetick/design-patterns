from .pattern import AbstractTechnicalStation, BaseEngine, BaseMechanic


class DieselEngine(BaseEngine):
    """Дизельный двигатель."""


class GasolineEngine(BaseEngine):
    """Бензиновый двигатель."""


class TurboEngine(BaseEngine):
    """Турбированный двигатель."""


class DieselMechanic(BaseMechanic):
    """Чинила дизельных двигателей."""

    def __init__(self, name: str, service_type: str = 'Дизель') -> None:
        super().__init__(name, service_type)


class GasolineMechanic(BaseMechanic):
    """Чинила бензиновых двигателей."""

    def __init__(self, name: str, service_type: str = 'Бензин') -> None:
        super().__init__(name, service_type)


class TurboMechanic(BaseMechanic):
    """Чинила турбо двигателей."""

    def __init__(self, name: str, service_type: str = 'Турбо') -> None:
        super().__init__(name, service_type)


class TechnicalStation1(AbstractTechnicalStation):
    """Техническая станция №1."""

    @classmethod
    def call_mechanic(cls, engine: BaseEngine) -> BaseMechanic | None:
        """Фабричный метод вызова механика на станции №1."""

        mechanic = None
        if isinstance(engine, DieselEngine):
            mechanic = DieselMechanic(name='Коля')
        elif isinstance(engine, GasolineEngine):
            mechanic = GasolineMechanic(name='Толя')
        elif isinstance(engine, TurboEngine):
            mechanic = TurboMechanic(name='Оля')

        return mechanic
