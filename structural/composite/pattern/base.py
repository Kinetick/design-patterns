from .abc import AbstractNetworkComponent


class BaseNetworkComponent(AbstractNetworkComponent):
    """Базовый класс для всех компонентов сети."""

    def __init__(self, network_name: str) -> None:
        self._parent = None
        self._name = network_name
        self._children: dict[str, AbstractNetworkComponent] = {}

    @property
    def root(self) -> AbstractNetworkComponent:
        root_component = self
        if self.parent is not None:
            root_component = self.parent.root

        return root_component

    @property
    def parent(self) -> AbstractNetworkComponent | None:
        return self._parent

    @parent.setter
    def parent(self, parent: AbstractNetworkComponent | None) -> None:
        parent_constraint = (
            isinstance(parent, AbstractNetworkComponent) or parent is None
        )
        if not parent_constraint:
            raise TypeError

        self._parent = parent

    @property
    def name(self) -> str:
        return self._name

    @property
    def children(self) -> list[AbstractNetworkComponent] | None:
        return list(self._children.values())

    def find_component(self, name: str) -> AbstractNetworkComponent | None:
        exists_component = self._children.get(name)
        if not exists_component:
            for child in self._children.values():
                exists_component = child.find_component(name=name)

        return exists_component


class BaseRouterComponent(BaseNetworkComponent):
    """Базовый класс маршрутизатора."""

    def add_component(self, component: AbstractNetworkComponent) -> None:
        exists_component = self.root.find_component(name=component.name)
        if exists_component:
            parent_name = (
                exists_component.parent.name
                if exists_component.parent
                else exists_component.parent
            )
            print(
                f"""
                Ошибка добавления компонента!
                Имя коллизии: {exists_component.name}
                Имя родителя: {parent_name}
                """
            )
        else:
            component.parent = self
            self._children[component.name] = component

    def remove_component(self, name: str) -> AbstractNetworkComponent | None:
        exists_component = self.root.find_component(name=name)
        if exists_component:
            if exists_component.parent is self:
                self._children.pop(exists_component.name)
            elif exists_component.parent:
                exists_component.parent.remove_component(name=name)

        return exists_component


class BasePCComponent(BaseNetworkComponent):
    """Базовый класс персонального компьютера."""

    def remove_component(self, name: str) -> AbstractNetworkComponent | None:
        raise NotImplementedError

    def add_component(self, component: AbstractNetworkComponent) -> None:
        raise NotImplementedError


class BaseMobileComponent(BaseNetworkComponent):
    """Базовый класс мобильного телефона."""

    def remove_component(self, name: str) -> AbstractNetworkComponent | None:
        raise NotImplementedError

    def add_component(self, component: AbstractNetworkComponent) -> None:
        raise NotImplementedError
