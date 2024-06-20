from .pattern import BaseEngine, InheritanceEnginePrototype

__all__ = [
    "InheritanceInLineEngine",
    "InheritanceRadialEngine",
    "InheritanceVEngine",
    "InLineEngine",
    "VEngine",
    "RadialEngine",
]


class InheritanceInLineEngine(InheritanceEnginePrototype):
    """Рядный двигатель через наследование от прототипа."""

    ...


class InheritanceVEngine(InheritanceEnginePrototype):
    """V-образный двигатель через наследование от прототипа."""

    ...


class InheritanceRadialEngine(InheritanceEnginePrototype):
    """Радиальный двигатель через наследование от прототипа."""

    ...


class InLineEngine(BaseEngine):
    """Рядный двигатель через наследование от базового класса."""

    ...


class VEngine(BaseEngine):
    """V-образный двигатель через наследование от базового класса."""

    ...


class RadialEngine(BaseEngine):
    """Радиальный двигатель через наследование от базового класса."""

    ...
