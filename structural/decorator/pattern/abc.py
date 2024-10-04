from abc import ABC, abstractmethod


class AbstractCharacter(ABC):
    """Описание интерфейса персонажа."""

    @property
    @abstractmethod
    def attack_parameter(self) -> int:
        """Показатель атаки персонажа."""

        ...

    @attack_parameter.setter
    @abstractmethod
    def attack_parameter(self, new_attack: int) -> None:
        """Показатель атаки персонажа."""

        ...

    @property
    @abstractmethod
    def defense_parameter(self) -> int:
        """Показатель защиты персонажа."""

        ...

    @defense_parameter.setter
    @abstractmethod
    def defense_parameter(self, new_defense: int) -> None:
        """Показатель защиты персонажа."""

        ...

    @abstractmethod
    def attack(self, enemy: "AbstractCharacter") -> int:
        """Интерфейс атаки противника."""

        ...

    @abstractmethod
    def defense(self, enemy: "AbstractCharacter") -> int:
        """Интерфейс защиты от атаки противника."""

        ...
