from copy import copy, deepcopy
from typing import Self

from .abc import AbstractRegisterPrototype, T


class BaseCopier:
    """Базовый класс копира."""

    def clone(self, is_shallow: bool = False) -> Self:
        """Интерфейс инициации копии."""

        return copy(self) if is_shallow else deepcopy(self)

    def __copy__(self) -> Self:
        """Интерфейс поверхностной копии."""

        current_class = self.__class__
        new_object = current_class.__new__(current_class)

        for k_attribute in dir(self):
            if not (
                k_attribute.startswith("_abc") or k_attribute.startswith("__")
            ):
                v_attribute = getattr(self, k_attribute)
                setattr(new_object, k_attribute, v_attribute)

        return new_object

    def __deepcopy__(self, memoization: dict) -> Self:
        """Интерфейс глубокой копии."""

        memoization = memoization if memoization else {}
        self_id = id(self)
        new_object = memoization.get(self_id)

        if new_object is None:
            current_class = self.__class__
            new_object = current_class.__new__(current_class)
            memoization[self_id] = new_object

            for k_attribute in dir(self):
                if not k_attribute.startswith("__"):
                    v_attribute = getattr(self, k_attribute)
                    setattr(
                        new_object,
                        k_attribute,
                        deepcopy(v_attribute, memoization),
                    )

        return new_object


# * Базовый копир не нуждается в инициализации, поэтому его можно использовать
# * как миксин.
class BaseEngine(BaseCopier):
    """Базовый класс двигателя."""

    def __init__(self, cylinder_list: list[int] | None) -> None:
        self._cylinders = cylinder_list

    @property
    def cylinders(self) -> list[int] | None:
        """Порядок работы цилиндров."""

        return self._cylinders

    @cylinders.setter
    def cylinders(self, new_cylinders: list[int] | None) -> None:
        self._cylinders = new_cylinders

    def __str__(self) -> str:
        description = f"""
            Тип двигателя: {self.__class__.__name__}
            Порядок работы цилиндров: {self._cylinders}
        """

        return description


class BaseRegisterPrototype(AbstractRegisterPrototype[T]):
    """Базовый класс регистратора прототипов двигателя."""

    def __init__(self, registered_map: dict[str, T] | None = None) -> None:
        self._registered_map = registered_map if registered_map else {}

    def register_copier(self, name_copier: str, copier: T) -> None:
        self._registered_map[name_copier] = copier

    def unregister_copier(self, name_copier: str) -> T | None:
        return self._registered_map.pop(name_copier, None)

    def clone(self, name_copier: str, is_shallow: bool = False) -> T:
        copier = self._registered_map[name_copier]

        return copier.clone(is_shallow)
