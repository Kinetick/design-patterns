from ..pattern.base import (
    BaseCommand,
    BaseCommandInterpreter,
    BaseManager,
    BaseNotProtocolCommand,
    BaseProtocolCommand,
    StopInterpret,
)


class MicroclimateManager(BaseManager):
    """Объект управления микроклиматом."""

    ...


class LightingManager(BaseManager):
    """Объект управления светом."""

    ...


class WindowCleanerManager(BaseManager):
    """Объект управления очистителем стекол."""

    ...


class MicroclimateManagementCommand(BaseProtocolCommand):
    """Команда управления микроклиматом."""

    ...


class LightingManagementCommand(BaseProtocolCommand):
    """Команда управления светом."""

    ...


class WindowCleanerManagementCommand(BaseProtocolCommand):
    """Команда управления очистителем стекол."""

    ...


class UndoCommand(BaseNotProtocolCommand):
    """Команда отмены буферизованной команды."""

    def execute(self) -> None:
        if not self._buffer:
            print("Нет команд для отмены, буфер пустой.")

        _, command = self._buffer.popitem()
        command.cancel()


class RedoCommand(BaseNotProtocolCommand):
    """Команда повторения буферизованной команды."""

    def execute(self) -> None:
        if not self._buffer:
            print("Нет команды для повторения, буфер пустой.")

        command_name, command = self._buffer.popitem()
        self._buffer[command_name] = command
        command.execute()


class HistoryCommand(BaseCommand):
    """Команда вывода истории команд."""

    def __init__(self, history: dict[int, str], *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._history = history

    def execute(self) -> None:
        for index, command in self._history.items():
            print(f"Индекс [{index}] :: Имя команды: [{command}]")


class ExitCommand(BaseCommand):
    """Команда выхода."""

    def execute(self) -> None:
        raise StopInterpret.create_successful()


command_light = LightingManagementCommand(
    receiver=LightingManager(), name="light"
)
command_microclimate = MicroclimateManagementCommand(
    receiver=MicroclimateManager(), name="microclimate"
)
command_window_cleaner = WindowCleanerManagementCommand(
    receiver=WindowCleanerManager(), name="window_cleaner"
)
commands = {
    "light": command_light,
    "microclimate": command_microclimate,
    "window_cleaner": command_window_cleaner,
}
buffer = {}
history = {}

common_command_interpreter = BaseCommandInterpreter(
    buffer=buffer, history=history, commands=commands
)
