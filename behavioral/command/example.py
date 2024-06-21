from .pattern import AbstractCommand, AbstractInvoker


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


class BaseManager:
    """Базовый класс объекта управления."""

    def __init__(self) -> None:
        self._state = None

    def __str__(self) -> str:
        """Текущее состояние устройства."""
        description = f"""
            Тип сервиса: {self.__class__.__name__}
            Сервис включен: {self._state}
        """

        return description


class MicroclimateManager(BaseManager):
    """Объект управления микроклиматом."""

    def on_microclimate(self) -> None:
        """Интерфейс включения системы микроклимата."""
        self._state = True
        print(self)

    def off_microclimate(self) -> None:
        """Интерфейс отключения системы микроклимата."""
        self._state = False
        print(self)


class LightingManager(BaseManager):
    """Объект управления светом."""

    def on_lighting(self) -> None:
        """Интерфейс включения света."""
        self._state = True
        print(self)

    def off_lighting(self) -> None:
        """Интерфейс выключения света."""
        self._state = False
        print(self)


class WindowCleanerManager(BaseManager):
    """Объект управления очистителем стекол."""

    def on_cleaner(self) -> None:
        """Интерфейс включения очистителя стекол."""
        self._state = True
        print(self)

    def off_cleaner(self) -> None:
        """Интерфейс отключения очистителя стекол."""
        self._state = False
        print(self)


class MicroclimateManagementCommand(AbstractCommand):
    """Команда управления микроклиматом."""

    def __init__(self, receiver: MicroclimateManager) -> None:
        self._receiver = receiver
        self._is_buffered = True
        self._name = "microclimate"

    @property
    def is_buffered(self) -> bool:
        return self._is_buffered

    @property
    def name(self) -> str:
        return self._name

    def execute(self) -> None:
        self._receiver.on_microclimate()

    def cancel(self) -> None:
        self._receiver.off_microclimate()


class LightingManagementCommand(AbstractCommand):
    """Команда управления светом."""

    def __init__(self, receiver: LightingManager) -> None:
        self._receiver = receiver
        self._buffered = True
        self._name = "lighter"

    @property
    def is_buffered(self) -> bool:
        return self._buffered

    @property
    def name(self) -> str:
        return self._name

    def execute(self) -> None:
        self._receiver.on_lighting()

    def cancel(self) -> None:
        self._receiver.off_lighting()


class WindowCleanerManagementCommand(AbstractCommand):
    """Команда управления очистителем стекол."""

    def __init__(self, receiver: WindowCleanerManager) -> None:
        self._receiver = receiver
        self._is_buffered = True
        self._name = "cleaner"

    @property
    def is_buffered(self) -> bool:
        return self._is_buffered

    @property
    def name(self) -> str:
        return self._name

    def execute(self) -> None:
        self._receiver.on_cleaner()

    def cancel(self) -> None:
        self._receiver.off_cleaner()


class UndoCommand(AbstractCommand):
    """Команда отмены буферизованной команды."""

    def __init__(self, buffer: dict[str, AbstractCommand]) -> None:
        self._buffer = buffer
        self._is_buffered = False
        self._name = "undo"

    @property
    def is_buffered(self) -> bool:
        return self._is_buffered

    @property
    def name(self) -> str:
        return self._name

    def execute(self) -> None:
        if not self._buffer:
            print("Нет команд для отмены, буфер пустой.")
            return None
        _, command = self._buffer.popitem()
        command.cancel()

    def cancel(self) -> None:
        raise NotImplementedError


class RedoCommand(AbstractCommand):
    """Команда повторения буферизованной команды."""

    def __init__(self, buffer: dict[str, AbstractCommand]) -> None:
        self._buffer = buffer
        self._is_buffered = False
        self._name = "redo"

    @property
    def is_buffered(self) -> bool:
        return self._is_buffered

    @property
    def name(self) -> str:
        return self._name

    def execute(self) -> None:
        if not self._buffer:
            print("Нет команды для повторения, буфер пустой.")
            return None
        command_name, command = self._buffer.popitem()
        self._buffer[command_name] = command
        command.execute()

    def cancel(self) -> None:
        raise NotImplementedError


class HistoryCommand(AbstractCommand):
    """Команда вывода истории команд."""

    def __init__(self, history: dict[int, str]) -> None:
        self._history = history
        self._is_buffered = False
        self._name = "history"

    @property
    def is_buffered(self) -> bool:
        return self._is_buffered

    @property
    def name(self) -> str:
        return self._name

    def execute(self) -> None:
        for index, command in self._history.items():
            print(f"Индекс [{index}] :: Имя команды: [{command}]")

    def cancel(self) -> None:
        raise NotImplementedError


class ExitCommand(AbstractCommand):
    """Команда выхода."""

    def __init__(self) -> None:
        self._is_buffered = False
        self._name = "exit"

    @property
    def is_buffered(self) -> bool:
        return self._is_buffered

    @property
    def name(self) -> str:
        return self._name

    def execute(self) -> None:
        raise StopInterpret.create_successful()

    def cancel(self) -> None:
        raise NotImplementedError


class CommandInterpreter(AbstractInvoker):
    """Интерпретатор команд управления устройствами."""

    def __init__(
        self,
        buffer: dict[str, AbstractCommand],
        history: dict[int, str],
        commands: dict[str, AbstractCommand] | None = None,
    ) -> None:
        self._commands = commands or {}
        self._buffer = buffer
        self._history = history

    def set_command(self, command: AbstractCommand) -> None:
        self._commands[command.name] = command

    def unset_command(self, command_name: str) -> AbstractCommand | None:
        return self._commands.pop(command_name, None)

    def input_command(self) -> AbstractCommand | None:
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
