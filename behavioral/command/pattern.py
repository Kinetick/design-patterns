from abc import ABC, abstractmethod


class AbstractCommand(ABC):
    """Описание интерфейса команды."""

    @abstractmethod
    def execute(self) -> None:
        """Интерфейс запуска команды."""
        ...

    @abstractmethod
    def cancel(self) -> None:
        """Интерфейс отмены команды."""
        ...


class AbstractInvoker(ABC):
    """Описание интерфейса инициатора команд."""

    @abstractmethod
    def input_command(self) -> AbstractCommand | None:
        """Интерфейс ввода команды."""
        ...

    @abstractmethod
    def set_command(self, command: AbstractCommand) -> None:
        """Интерфейс постановки команды в список допустимых команд."""
        ...

    @abstractmethod
    def unset_command(self, command_name: str) -> AbstractCommand | None:
        """Интерфейс отзыва команды из списка допустимых команд."""
        ...

    @abstractmethod
    def run_invoker(self) -> None:
        """Интерфейс запуска инициатора команд."""


class BaseCommand(AbstractCommand):
    """Базовый класс команды."""

    def __init__(
        self, name: str, is_buffered: bool, receiver: "BaseManager | None"
    ) -> None:
        self._name = name.casefold()
        self._is_buffered = is_buffered
        self._receiver = receiver

    @property
    def is_buffered(self) -> bool:
        """Свойство буферизации команды."""
        return self._is_buffered

    @property
    def name(self) -> str:
        """Имя команды."""
        return self._name


class BaseManager:
    """Базовый класс объекта управления."""

    def __init__(self) -> None:
        self._state = None

    @property
    def state(self) -> bool | None:
        """Текущее состояние объекта."""
        return self._state

    def on_state(self) -> None:
        """Интерфейс изменения текущего состояния объекта на 'ON'."""
        self._state = True
        print(self)

    def off_state(self) -> None:
        """Интерфейс изменения текущего состояния объекта на 'OFF'."""
        self._state = False
        print(self)

    def __str__(self) -> str:
        """Текущее состояние устройства."""
        description = f"""
            Тип сервиса: {self.__class__.__name__}
            Сервис включен: {self._state}
        """

        return description
