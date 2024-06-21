"""
Поведенческий паттерн проектирования - команда.

pattern.py
    Паттерн позволяет инкапсулировать вызов конкретной команды в отдельный
    объект. Таким образом клиент устанавливающий команду не знает ничего об
    исполнителе команды. Объект команды может параметризоваться и
    протоколироваться. Благодаря инкапсуляции обеспечивается единый интерфейс
    запуска и отмены команды, несмотря на интерфейс получателя команды.

example.py
    В качестве примера можно написать интерпретатор команд для работы с
    несколькими устройствами. В качестве участников паттерна выступают:
        Получатель команды:
            - объект управления микроклиматом
            - объект управления светом
            - объект управления очистителем стекол

        Команды:
            - команда объекта управления микроклиматом
            - команда объекта управления светом
            - команда объекта управления очистителем стекол
            - команда отмены последней запущенной команды
            - команда повтора последней запущенной команды
            - команда печати истории запуска команд
            - команда завершения работы интерпретатора

        Инициатор:
            - интерпретатор команд

        Клиент:
            - его реализации нет

"""

from .example import (
    CommandInterpreter,
    ExitCommand,
    HistoryCommand,
    LightingManagementCommand,
    LightingManager,
    MicroclimateManagementCommand,
    MicroclimateManager,
    RedoCommand,
    UndoCommand,
    WindowCleanerManagementCommand,
    WindowCleanerManager,
)

__all__ = [
    "CommandInterpreter",
    "ExitCommand",
    "LightingManagementCommand",
    "LightingManager",
    "MicroclimateManagementCommand",
    "MicroclimateManager",
    "RedoCommand",
    "UndoCommand",
    "WindowCleanerManagementCommand",
    "WindowCleanerManager",
    "HistoryCommand",
]
