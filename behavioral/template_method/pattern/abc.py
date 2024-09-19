from abc import ABC, abstractmethod


class AbstractFileDownloader(ABC):
    """Описание интерфейса загрузчика файлов."""

    @abstractmethod
    def connect_to_storage(self) -> dict[str, str]:
        """Интерфейс подключения к хранилищу."""
        ...

    @abstractmethod
    def search_file(
        self, file_name: str, storage_view: dict[str, str]
    ) -> tuple[str, str]:
        """Интерфейс поиска файла в хранилище."""
        ...

    def write_to_memory(self, file_data: tuple[str, str]) -> None:
        """Интерфейс записи данных файла в память."""
        ...

    def write_to_external_storage(self, external_storage: dict) -> None:
        """Интерфейс записи файла на внешнее устройство."""
        ...

    def download_file(self, file_name: str, external_storage: dict) -> None:
        """Основной интерфейс загрузки файла."""
        ...
