from .pattern import (
    AbstractInvoker,
    BaseCommand,
    BaseManager,
)


class StopInterpret(Exception):
    """Завершение интерпретации команд."""

    def __init__(self, message: str, exit_code: int) -> None:
        self.message = message
        self.exit_code = exit_code

    @classmethod
    def create_successful(cls) -> "StopInterpret":
        """Фабричный метод успешного завершения интерпретатора."""
        message = "Завершение работы интерпретатора."
        exit_code = 0

        return cls(message=message, exit_code=exit_code)

    def __str__(self) -> str:
        """Состояние завершения интерпретатора."""
        description = f"Сообщение: {self.message} :: Код: {self.exit_code}"

        return description


class MicroclimateManager(BaseManager):
    """Объект управления микроклиматом."""


class LightingManager(BaseManager):
    """Объект управления светом."""


class WindowCleanerManager(BaseManager):
    """Объект управления очистителем стекол."""


class MicroclimateManagementCommand(BaseCommand):
    """Команда управления микроклиматом."""

    def execute(self) -> None:
        if self._receiver:
            turn_on = not self._receiver.state
            self._receiver.on_state if turn_on else self._receiver.off_state()

    def cancel(self) -> None:
        if self._receiver:
            self._receiver.off_state()


class LightingManagementCommand(BaseCommand):
    """Команда управления светом."""

    def execute(self) -> None:
        if self._receiver:
            turn_on = not self._receiver.state
            self._receiver.on_state if turn_on else self._receiver.off_state()

    def cancel(self) -> None:
        if self._receiver:
            self._receiver.off_state()


class WindowCleanerManagementCommand(BaseCommand):
    """Команда управления очистителем стекол."""

    def execute(self) -> None:
        if self._receiver:
            turn_on = not self._receiver.state
            self._receiver.on_state if turn_on else self._receiver.off_state()

    def cancel(self) -> None:
        if self._receiver:
            self._receiver.off_state()


class UndoCommand(BaseCommand):
    """Команда отмены буферизованной команды."""

    def __init__(
        self, buffer: dict[str, BaseCommand], *args, **kwargs
    ) -> None:
        super().__init__(*args, **kwargs)
        self._buffer = buffer

    def execute(self) -> None:
        if not self._buffer:
            print("Нет команд для отмены, буфер пустой.")

        _, command = self._buffer.popitem()
        command.cancel()

    def cancel(self) -> None:
        raise NotImplementedError


class RedoCommand(BaseCommand):
    """Команда повторения буферизованной команды."""

    def __init__(
        self, buffer: dict[str, BaseCommand], *args, **kwargs
    ) -> None:
        super().__init__(*args, **kwargs)
        self._buffer = buffer

    def execute(self) -> None:
        if not self._buffer:
            print("Нет команды для повторения, буфер пустой.")

        command_name, command = self._buffer.popitem()
        self._buffer[command_name] = command
        command.execute()

    def cancel(self) -> None:
        raise NotImplementedError


class HistoryCommand(BaseCommand):
    """Команда вывода истории команд."""

    def __init__(self, history: dict[int, str], *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._history = history

    def execute(self) -> None:
        for index, command in self._history.items():
            print(f"Индекс [{index}] :: Имя команды: [{command}]")

    def cancel(self) -> None:
        raise NotImplementedError


class ExitCommand(BaseCommand):
    """Команда выхода."""

    def execute(self) -> None:
        raise StopInterpret.create_successful()

    def cancel(self) -> None:
        raise NotImplementedError


class CommandInterpreter(AbstractInvoker):
    """Интерпретатор команд управления устройствами."""

    def __init__(
        self,
        buffer: dict[str, BaseCommand],
        history: dict[int, str],
        commands: dict[str, BaseCommand] | None = None,
    ) -> None:
        self._commands = commands or {}
        self._buffer = buffer
        self._history = history

    def set_command(self, command: BaseCommand) -> None:
        self._commands[command.name] = command

    def unset_command(self, command_name: str) -> BaseCommand | None:
        return self._commands.pop(command_name, None)

    def input_command(self) -> BaseCommand | None:
        command_name = input(">> ").casefold()
        command = self._commands.get(command_name)
        if not command:
            print(f"Команда '{command_name}' не найдена.")

        return command

    def run_invoker(self) -> None:
        index = 0
        while True:
            command = self.input_command()
            if not command:
                continue

            try:
                command.execute()
            except StopInterpret as e_stop:
                print(e_stop)
                exit(e_stop.exit_code)

            if command.is_buffered:
                self._buffer[command.name] = command
                self._history[index] = command.__class__.__name__
                index += 1
