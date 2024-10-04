from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .base import AsyncResponse, SyncResponse


class AbstractSyncDownloader(ABC):
    """Описание интерфейса синхронного загрузчика"""

    @abstractmethod
    def sync_download(self, urls: list[str]) -> list["SyncResponse"]:
        """Интерфейс синхронной загрузки документов."""

        ...


class AbstractAsyncDownloader(ABC):
    """Описание интерфейса асинхронного загрузчика."""

    @abstractmethod
    def async_download(self, resources: list[str]) -> list["AsyncResponse"]:
        """Интерфейс асинхронной загрузки документов."""

        ...


class AbstractClient(ABC):
    """Описание интерфейса клиента."""

    @abstractmethod
    def add_url(self, url: str) -> None:
        """Интерфейс добавления URL для загрузки."""

        ...

    @abstractmethod
    def download(
        self, downloader: AbstractSyncDownloader
    ) -> list["SyncResponse"]:
        """Интерфейс инициации загрузки документов."""

        ...
