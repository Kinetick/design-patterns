from abc import ABC, abstractmethod


class AbstractNetworkComponent(ABC):
    """Описание интерфейса компонента сети."""

    @property
    @abstractmethod
    def root(self) -> "AbstractNetworkComponent":
        """Корневой элемент."""

        ...

    @property
    @abstractmethod
    def name(self) -> str:
        """Имя компонента в сети."""

        ...

    @property
    @abstractmethod
    def children(self) -> list["AbstractNetworkComponent"] | None:
        """Дочерние компоненты."""

        ...

    @property
    @abstractmethod
    def parent(self) -> "AbstractNetworkComponent | None":
        """Родительский компонент."""

        ...

    @parent.setter
    @abstractmethod
    def parent(self, parent: "AbstractNetworkComponent | None") -> None:
        """Родительский компонент."""

        ...

    @abstractmethod
    def add_component(self, component: "AbstractNetworkComponent") -> None:
        """Интерфейс добавления одного компонента в другой."""

        ...

    @abstractmethod
    def find_component(self, name: str) -> "AbstractNetworkComponent | None":
        """Интерфейс поиска компонента в сети по имени."""

        ...

    @abstractmethod
    def remove_component(self, name: str) -> "AbstractNetworkComponent | None":
        """Интерфейс удаления компонента из сети."""

        ...
