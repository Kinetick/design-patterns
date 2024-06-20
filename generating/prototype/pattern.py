from copy import copy, deepcopy


class InheritanceEnginePrototype:
    """Описания интерфейса прототипа двигателя через наследование."""

    def __init__(self, cylinder_list: list[int]) -> None:
        self.cylinders = cylinder_list

    def clone(self, is_shallow: bool = False) -> "InheritanceEnginePrototype":
        """Интерфейс копирования объекта самим себя."""
        copied_engine = copy(self) if is_shallow else deepcopy(self)

        return copied_engine

    def __str__(self) -> str:
        """Общая информация о двигателе."""
        description = f"""
            Тип двигателя: {self.__class__.__name__}
            Общее кол-во цилиндров: {self.cylinders}
        """

        return description

    def __copy__(self) -> "InheritanceEnginePrototype":
        """Метод поверхностного копирования объекта."""
        current_class = self.__class__
        new_object = current_class.__new__(current_class)
        new_object.__init__(self.cylinders)

        return new_object

    def __deepcopy__(self, memoization: dict) -> "InheritanceEnginePrototype":
        """Метод глубокого копирования объекта."""
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


class BaseEngine:
    """Базовый класс двигателя."""

    def __init__(self, cylinder_list: list[int]) -> None:
        self.cylinders = cylinder_list

    def __str__(self) -> str:
        """Общая информация о двигателе."""
        description = f"""
            Тип двигателя: {self.__class__.__name__}
            Общее кол-во цилиндров: {self.cylinders}
        """

        return description

    def __copy__(self) -> "BaseEngine":
        """Метод поверхностного копирования объекта."""
        current_class = self.__class__
        new_object = current_class.__new__(current_class)
        new_object.__init__(self.cylinders)

        return new_object

    def __deepcopy__(self, memoization: dict) -> "BaseEngine":
        """Метод глубокого копирования объекта."""
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


class RegisterEnginePrototype:
    """Класс прототипа с регистрацией объектов."""

    _REGISTERED_ENGINES = {}

    @classmethod
    def register_engine(cls, name_engine: str, engine: BaseEngine) -> None:
        """Интерфейс регистрации двигателя."""
        cls._REGISTERED_ENGINES[name_engine] = engine

    @classmethod
    def unregister_engine(cls, name_engine: str) -> BaseEngine | None:
        """Интерфейс исключения двигателя из регистра."""
        engine = cls._REGISTERED_ENGINES.pop(name_engine, None)

        return engine

    @classmethod
    def clone(
        cls, name_engine: str, is_shallow: bool = False
    ) -> BaseEngine | None:
        """Интерфейс клонирования объекта двигателя."""
        engine = cls._REGISTERED_ENGINES.get(name_engine)
        result = copy(engine) if is_shallow else deepcopy(engine)

        return result
