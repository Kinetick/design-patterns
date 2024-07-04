from .pattern import AbstractFileDownloader


class CloudFileDownloader(AbstractFileDownloader):
    """Облачный загрузчик файла."""

    def connect_to_storage(self) -> dict[str, str]:
        """Интерфейс подключения к облачному хранилищу."""
        print("Установка подключения к облачному хранилищу...", end=" ")
        cloud_storage_view = self._storage
        print("OK.")

        return cloud_storage_view

    def search_file(
        self, file_name: str, storage_view: dict[str, str]
    ) -> tuple[str, str]:
        """Интерфейс поиска файла в облачном хранилище."""
        print("Поиск файла в облачном хранилище...", end=" ")
        file_data = storage_view.get(file_name)
        if file_data is None:
            print("FAIL.")
            raise FileNotFoundError(f"Файл с именем: {file_name} не найден.")
        print("OK.")

        return file_name, file_data


class LocalFileDownloader(AbstractFileDownloader):
    """Локальный загрузчик файла."""

    def connect_to_storage(self) -> dict[str, str]:
        """Интерфейс подключения к файловой системе."""
        print("Монтирование загрузчика в корень системы...", end=" ")
        system_storage_view = self._storage
        print("OK.")

        return system_storage_view

    def search_file(
        self, file_name: str, storage_view: dict[str, str]
    ) -> tuple[str, str]:
        """Интерфейс поиска файла в локальной системе."""
        print("Поиск файла на локальном компьютере...", end=" ")
        file_data = storage_view.get(file_name)
        if file_data is None:
            print("FAIL.")
            raise FileNotFoundError(f"Файл с именем: {file_name} не найден.")
        print("OK.")

        return file_name, file_data
