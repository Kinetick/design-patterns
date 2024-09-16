from ..pattern.base import BaseEngine, BaseRegisterPrototype


class InLineEngine(BaseEngine):
    """Рядный двигатель."""

    ...


class VEngine(BaseEngine):
    """V-образный двигатель."""

    ...


engine_register_prototype = BaseRegisterPrototype[BaseEngine]()
engine_register_prototype.register_copier(
    name_copier="inline_engine", copier=InLineEngine(cylinder_list=[1, 2, 3])
)
engine_register_prototype.register_copier(
    name_copier="v_engine", copier=VEngine(cylinder_list=[1, 3, 2, 4])
)
