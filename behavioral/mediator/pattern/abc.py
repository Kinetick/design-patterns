from abc import ABC, abstractmethod


class AbstractService(ABC):
    """Описание интерфейса сервиса."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Имя сервиса."""

        ...

    @abstractmethod
    def send_message(self, message: str) -> None:
        """Интерфейс отправки сообщения."""

        ...

    @abstractmethod
    def receive_message(self, message: str) -> None:
        """Интерфейс получения сообщения."""

        ...


class AbstractMessageExchanger(ABC):
    """Интерфейс обменника сообщениями."""

    @abstractmethod
    def push_message(self, topic: str, message: str) -> None:
        """Интерфейс проталкивания сообщения."""

        ...

    @abstractmethod
    def register_service(self, topic: str, service: AbstractService) -> None:
        """Интерфейс регистрации сервиса."""

        ...

    @abstractmethod
    def unregister_service(
        self, service_name: str, topics: list[str] | None = None
    ) -> None:
        """Интерфейс разрегистрации сервиса."""

        ...
