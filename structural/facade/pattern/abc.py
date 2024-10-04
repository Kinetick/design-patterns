from abc import ABC, abstractmethod


class AbstractDBManager(ABC):
    """Описание интерфейса менеджера БД."""

    @abstractmethod
    def get_file_path(self, file_index: int) -> str | None:
        """Интерфейс получения пути к файлу по индексу."""

        ...


class AbstractFileStorageManager(ABC):
    """Описание интерфейса менеджера файлового хранилища."""

    @abstractmethod
    def get_file(self, file_path: str | None) -> str | None:
        """Интерфейс получения файла из хранилища."""

        ...


class AbstractFileSystemManager(ABC):
    """Описание интерфейса загрузка файловой системы."""

    @abstractmethod
    def write_file(self, file: str | None, fs_path: str) -> bool:
        """Интерфейс записи файла в файловую систему."""

        ...


class AbstractFileManagerFacade(ABC):
    """Описание интерфейса фасада менеджера файлов."""

    @property
    @abstractmethod
    def db_manager(self) -> AbstractDBManager:
        """Менеджер БД."""

        ...

    @property
    @abstractmethod
    def st_manager(self) -> AbstractFileStorageManager:
        """Менеджер файлового хранилища."""

        ...

    @property
    @abstractmethod
    def fs_manager(self) -> AbstractFileSystemManager:
        """Менеджер файловой системы."""

        ...

    @abstractmethod
    def download(self, file_index: int, fs_path: str) -> bool:
        """Интерфейс загрузки файла на диск."""

        ...
