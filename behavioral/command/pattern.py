from abc import ABC, abstractmethod


class AbstractCommand(ABC):
    """Описание интерфейса команды."""

    @property
    @abstractmethod
    def is_buffered(self) -> bool:
        """Свойство буферизации команды."""
        ...

    @property
    @abstractmethod
    def name(self) -> str:
        """Имя команды."""
        ...

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
