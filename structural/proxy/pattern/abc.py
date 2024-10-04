from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .base import UserSession


class AbstractDBManager(ABC):
    """Описание интерфейса менеджера БД."""

    @abstractmethod
    def get_file_path(
        self, index: int, user_session: "UserSession"
    ) -> str | None:
        """Интерфейс получения пути файла по индексу."""

        ...

    @abstractmethod
    def add_file_path(
        self, index: int, path: str, user_session: "UserSession"
    ) -> None:
        """'Добавление пути к файлу в БД."""

        ...

    @abstractmethod
    def add_user(self, user_session: "UserSession") -> None:
        """Интерфейс добавления пользователя в СУБД."""

        ...


class AbstractCacheManager(ABC):
    """Описание интерфейса менеджера кеша."""

    @abstractmethod
    def get_file_path(self, index: int) -> str | None:
        """Интерфейс получения пути файла по индексу."""

        ...

    @abstractmethod
    def add_file_path(self, index: int, path: str) -> None:
        """Интерфейс добавления пути файла в кэш."""

        ...


class AbstractAuthManager(ABC):
    """Описание интерфейса менеджера авторизации."""

    @abstractmethod
    def check_permissions(self, user_session: "UserSession") -> bool:
        """Интерфейс проверки привилегий пользователя по маске."""

        ...

    @abstractmethod
    def add_user(
        self, user_session: "UserSession", permissions_mask: int
    ) -> None:
        """Интерфейс добавления пользователя в систему."""

        ...

    @abstractmethod
    def add_permissions(self, permissions_map: dict[int, bool]) -> None:
        """Интерфейс добавления привилегий в систему."""

        ...
