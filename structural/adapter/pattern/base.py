from random import randint
from typing import TypedDict

from .abc import (
    AbstractAsyncDownloader,
    AbstractClient,
    AbstractSyncDownloader,
)


class SyncResponse(TypedDict):
    """Модель результата синхронной загрузки документа."""

    resource: str
    status_code: int
    data: bytes


class AsyncResponse(TypedDict):
    """Модель результата асинхронной загрузки документа."""

    url: str
    response_code: int
    decoded_data: str


class BaseSyncDownloader(AbstractSyncDownloader):
    """Базовый класс синхронного загрузчика."""

    def sync_download(self, urls: list[str]) -> list[SyncResponse]:
        print(f"Синхронная загрузка: {len(urls)} документов.")

        result = []
        for url in urls:
            result.append(
                SyncResponse(
                    resource=url,
                    status_code=randint(100, 500),
                    data=bytes([randint(1, 255)]),
                )
            )

        return result


class BaseAsyncDownloader(AbstractAsyncDownloader):
    """Базовый класс асинхронного загрузчика."""

    def async_download(self, resources: list[str]) -> list[AsyncResponse]:
        print(f"Асинхронная загрузка: {len(resources)} документов.")

        # * Тут мы якобы забрасываем все в ThreadPool, но для примера это
        # * избыточно.
        result = []
        for resource in resources:
            result.append(
                AsyncResponse(
                    url=resource,
                    response_code=randint(100, 500),
                    decoded_data=str(randint(1, int(10e20))),
                )
            )

        return result


class BaseClient(AbstractClient):
    """Базовый класс клиента."""

    def __init__(self, urls: list[str] | None = None) -> None:
        self._urls = urls if urls else []

    def add_url(self, url: str) -> None:
        self._urls.append(url)

    def download(
        self, downloader: AbstractSyncDownloader
    ) -> list[SyncResponse]:
        return downloader.sync_download(urls=self._urls)
