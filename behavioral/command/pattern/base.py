from .abc import (
    AbstractCommand,
    AbstractInvoker,
    AbstractManager,
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


class BaseCommand(AbstractCommand):
    """Базовый класс команды."""

    def __init__(self, name: str, is_buffered: bool) -> None:
        self._name = name.casefold()
        self._is_buffered = is_buffered

    @property
    def is_buffered(self) -> bool:
        """Свойство буферизации команды."""
        return self._is_buffered

    @property
    def name(self) -> str:
        """Имя команды."""
        return self._name

    def cancel(self) -> None:
        raise NotImplementedError


class BaseProtocolCommand(BaseCommand):
    """Базовый класс протоколируемой команды."""

    def __init__(
        self,
        receiver: AbstractManager | None,
        is_buffered: bool = True,
        *args,
        **kwargs,
    ) -> None:
        super().__init__(is_buffered=is_buffered, *args, **kwargs)
        self._receiver = receiver

    def execute(self) -> None:
        if self._receiver:
            turn_on = not self._receiver.state
            self._receiver.on_state if turn_on else self._receiver.off_state()

    def cancel(self) -> None:
        if self._receiver:
            self._receiver.off_state()


class BaseNotProtocolCommand(BaseCommand):
    """Базовый класс не протоколируемой команды."""

    def __init__(
        self, buffer: dict[str, BaseCommand], *args, **kwargs
    ) -> None:
        super().__init__(*args, **kwargs)
        self._buffer = buffer


class BaseManager(AbstractManager):
    """Базовый класс объекта управления."""

    def __init__(self) -> None:
        self._state = None

    @property
    def state(self) -> bool | None:
        return self._state

    def on_state(self) -> None:
        self._state = True
        print(self)

    def off_state(self) -> None:
        self._state = False
        print(self)

    def __str__(self) -> str:
        """Текущее состояние устройства."""
        description = f"""
            Тип сервиса: {self.__class__.__name__}
            Сервис включен: {self._state}
        """

        return description


class BaseCommandInterpreter(AbstractInvoker):
    """Базовый интерпретатор команд управления устройствами."""

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
