from abc import ABC, abstractmethod


class AbstractFileDownloader(ABC):
    """Описание интерфейса загрузчика файлов."""

    def __init__(self, storage: dict[str, str]) -> None:
        self._storage = storage
        self._memory = {}

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
        print("Запись файла в память...", end=" ")
        self._memory[file_data[0]] = file_data[1]
        print("ОК.")

    def write_to_external_storage(self, external_storage: dict) -> None:
        """Интерфейс записи файла на внешнее устройство."""
        print("Загрузка данных из памяти...", end=" ")
        memorized_file = self._memory.popitem()
        print("OK.")
        print("Запись данных на внешний накопитель...", end=" ")
        external_storage[memorized_file[0]] = memorized_file[1]
        print("OK.")

    def download_file(self, file_name: str, external_storage: dict) -> None:
        """Основной интерфейс загрузки файла."""
        storage_view = self.connect_to_storage()
        file_data = self.search_file(file_name, storage_view)
        self.write_to_memory(file_data)
        self.write_to_external_storage(external_storage)
