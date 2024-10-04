from .abc import (
    AbstractDBManager,
    AbstractFileManagerFacade,
    AbstractFileStorageManager,
    AbstractFileSystemManager,
)


class BaseDBManager(AbstractDBManager):
    """Базовый класс менеджера БД."""

    def __init__(self, mok_database: dict[int, str]) -> None:
        self._database = mok_database

    def get_file_path(self, file_index: int) -> str | None:
        return self._database.get(file_index)


class BaseFileStorageManager(AbstractFileStorageManager):
    """Базовый класс менеджера файлового хранилища."""

    def __init__(self, mok_file_storage: dict[str, str]) -> None:
        self._storage = mok_file_storage

    def get_file(self, file_path: str | None) -> str | None:
        return self._storage.get(file_path) if file_path else file_path


class BaseFileSystemManager(AbstractFileSystemManager):
    """Базовый класс менеджера файловой системы."""

    def __init__(self, mok_file_system: dict[str, str]) -> None:
        self._file_system = mok_file_system

    def write_file(self, file: str | None, fs_path: str) -> bool:
        if file:
            self._file_system[fs_path] = file

        return fs_path in self._file_system


class BaseFileManagerFacade(AbstractFileManagerFacade):
    """Базовый класс фасада файлового менеджера."""

    def __init__(
        self,
        db_manager: AbstractDBManager,
        st_manager: AbstractFileStorageManager,
        fs_manager: AbstractFileSystemManager,
    ) -> None:
        self._db_manager = db_manager
        self._st_manager = st_manager
        self._fs_manager = fs_manager

    @property
    def db_manager(self) -> AbstractDBManager:
        return self._db_manager

    @property
    def st_manager(self) -> AbstractFileStorageManager:
        return self._st_manager

    @property
    def fs_manager(self) -> AbstractFileSystemManager:
        return self._fs_manager

    def download(self, file_index: int, fs_path: str) -> bool:
        file_path = self._db_manager.get_file_path(file_index=file_index)
        file_object = self._st_manager.get_file(file_path=file_path)

        return self._fs_manager.write_file(file=file_object, fs_path=fs_path)
