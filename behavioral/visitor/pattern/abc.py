from abc import ABC, abstractmethod


class AbstractDevice(ABC):
    """Описание интерфейса бытового прибора."""

    @property
    @abstractmethod
    def model(self) -> str:
        """Модель устройства."""

        ...

    @property
    @abstractmethod
    def dimensions(self) -> tuple[int, int, int]:
        """Габариты устройства."""

        ...

    @abstractmethod
    def accept(self, visitor: "AbstractBusVisitor") -> None:
        """Интерфейс инициации работы посетителя."""

        ...


class AbstractKettle(AbstractDevice):
    """Описание интерфейса чайника."""

    @property
    @abstractmethod
    def max_water_volume(self) -> float:
        """Максимальный объем воды в чайнике."""

        ...

    @property
    @abstractmethod
    def current_water_volume(self) -> float:
        """Текущий объем воды в чайнике."""

        ...

    @current_water_volume.setter
    @abstractmethod
    def current_water_volume(self, water: float) -> None:
        """Текущий объем воды в чайнике."""

        ...


class AbstractFridge(AbstractDevice):
    """Описание интерфейса холодильника."""

    @property
    @abstractmethod
    def chambers_count(self) -> int:
        """Кол-во камер в холодильнике."""

        ...

    @property
    @abstractmethod
    def non_freezer_min_degrees(self) -> int:
        """Минимальная температура не в морозильнике."""

        ...

    @property
    @abstractmethod
    def freezer_min_degrees(self) -> int:
        """Минимальная температура в морозильнике."""

        ...

    @property
    @abstractmethod
    def current_degrees(self) -> tuple[int, int]:
        """Текущая температура в морозилке и не морозилке."""

        ...

    @current_degrees.setter
    @abstractmethod
    def current_degrees(self, degrees: tuple[int, int]) -> None:
        """Текущая температура в морозилке и не морозилке."""

        ...


class AbstractWashing(AbstractDevice):
    """Описание интерфейса стиральной машины."""

    @property
    @abstractmethod
    def max_clothes_load(self) -> float:
        """Максимальная загрузка белья."""

        ...

    @property
    @abstractmethod
    def max_water_consumption(self) -> float:
        """Максимальный расход воды."""

        ...

    @property
    @abstractmethod
    def current_clothes_load(self) -> float:
        """Текущая загрузка одежды."""

        ...

    @current_clothes_load.setter
    @abstractmethod
    def current_clothes_load(self, clothes: float) -> None:
        """Текущая загрузка одежды."""

        ...


class AbstractBusVisitor(ABC):
    """Описание интерфейса абстрактного посетителя шины."""

    @abstractmethod
    def visit_fridge(self, fridge: AbstractFridge) -> None:
        """Интерфейс посещения холодильника."""

        ...

    @abstractmethod
    def visit_washing(self, washing: AbstractWashing) -> None:
        """Интерфейс посещения стиральной машины."""

        ...

    @abstractmethod
    def visit_kettle(self, kettle: AbstractKettle) -> None:
        """Интерфейс посещения чайника."""

        ...


class AbstractBus(ABC):
    """Описание интерфейса шины подключения бытовых устройств."""

    @abstractmethod
    def register_device(self, device: AbstractDevice) -> None:
        """Интерфейс регистрации/подключения устройства к шине."""

        ...

    @abstractmethod
    def unregister_device(self, model: str) -> None:
        """Интерфейс разрегистрации/отключения устройства от шины."""

        ...

    @abstractmethod
    def accept(self, visitor: AbstractBusVisitor) -> None:
        """Интерфейс приема посетителя."""

        ...
