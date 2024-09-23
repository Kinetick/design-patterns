from .abc import AbstractMessageExchanger, AbstractService


class BaseService(AbstractService):
    """Базовый класс сервиса."""

    def __init__(
        self, service_name: str, message_exchanger: AbstractMessageExchanger
    ) -> None:
        self._name = service_name
        self._exchanger = message_exchanger

    @property
    def name(self) -> str:
        return self._name

    def send_message(self, message: str) -> None:
        self._exchanger.push_message(topic=self.name, message=message)

    def receive_message(self, message: str) -> None:
        print(
            f"""
                Получено сообщение: {message}
                Получатель: {self.name}
            """
        )


class BaseMessageExchanger(AbstractMessageExchanger):
    """Базовый класс обменника сообщениями."""

    def __init__(
        self, routes_map: dict[str, dict[str, AbstractService]] | None = None
    ) -> None:
        self._routes_map = routes_map if routes_map else {}

    def register_service(self, topic: str, service: AbstractService) -> None:
        if topic not in self._routes_map:
            self._routes_map[topic] = {}

        self._routes_map[topic][service.name] = service

    def unregister_service(
        self, service_name: str, topics: list[str] | None = None
    ) -> None:
        if not topics:
            topics = list(self._routes_map)

        for topic in topics:
            if topic in self._routes_map:
                self._routes_map.pop(service_name, None)

    def push_message(self, topic: str, message: str) -> None:
        if topic in self._routes_map:
            for service in self._routes_map[topic].values():
                service.receive_message(message=message)
