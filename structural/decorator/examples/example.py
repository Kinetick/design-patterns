from ..pattern.abc import AbstractCharacter
from ..pattern.base import BaseDecorator


class AttackDecorator(BaseDecorator):
    def __init__(self, character: AbstractCharacter) -> None:
        super().__init__(character=character)
        self._character.attack_parameter += 1


class DefenseDecorator(BaseDecorator):
    def __init__(self, character: AbstractCharacter) -> None:
        super().__init__(character=character)
        self._character.defense_parameter += 1
