from .abc import AbstractCharacter


class BaseDecorator(AbstractCharacter):
    """Базовый класс декоратора персонажа."""

    def __init__(self, character: AbstractCharacter) -> None:
        self._character = character

    @property
    def attack_parameter(self) -> int:
        return self._character.attack_parameter

    @attack_parameter.setter
    def attack_parameter(self, new_attack: int) -> None:
        self._character.attack_parameter = new_attack

    @property
    def defense_parameter(self) -> int:
        return self._character.defense_parameter

    @defense_parameter.setter
    def defense_parameter(self, new_defense: int) -> None:
        self._character.defense_parameter = new_defense

    def attack(self, enemy: AbstractCharacter) -> int:
        return self._character.attack(enemy=enemy)

    def defense(self, enemy: AbstractCharacter) -> int:
        return self._character.defense(enemy=enemy)


class BaseCharacter(AbstractCharacter):
    """Базовый класс персонажа."""

    def __init__(
        self, attack_parameter: int, defense_parameter: int, name: str
    ) -> None:
        self._attack = attack_parameter
        self._defense = defense_parameter
        self._name = name

    @property
    def attack_parameter(self) -> int:
        return self._attack

    @attack_parameter.setter
    def attack_parameter(self, new_attack: int) -> None:
        delta_attack = new_attack - self._attack
        self._attack = new_attack

        buff_message = f"""
            Персонаж: {"_".join([self._name, str(id(self))])}
            Прибавка к атаке: {delta_attack}
            Итого атака: {self.attack_parameter}
        """
        print(buff_message)

    @property
    def defense_parameter(self) -> int:
        return self._defense

    @defense_parameter.setter
    def defense_parameter(self, new_defense: int) -> None:
        delta_defense = new_defense - self._defense
        self._defense = new_defense
        buff_message = f"""
            Персонаж: {"_".join([self._name, str(id(self))])}
            Прибавка к защите: {delta_defense}
            Итого атака: {self.defense_parameter}
        """
        print(buff_message)

    def attack(self, enemy: AbstractCharacter) -> int:
        pre_damage = self._attack - enemy.defense_parameter
        damage = pre_damage if pre_damage > 0 else 0
        print(damage)

        return damage

    def defense(self, enemy: AbstractCharacter) -> int:
        pre_damage = enemy.attack_parameter - self._defense
        damage = pre_damage if pre_damage > 0 else 0
        print(damage)

        return damage
