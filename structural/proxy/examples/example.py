from ..pattern.abc import (
    AbstractAuthManager,
    AbstractCacheManager,
    AbstractDBManager,
)
from ..pattern.base import (
    BaseAuthManager,
    BaseCacheManager,
    BaseDBManager,
    MokAuthDatabase,
    MokDatabase,
    UserSession,
)


class DBManagerProxy(AbstractDBManager):
    """Прокси объект менеджера БД."""

    def __init__(
        self,
        cache_manager: AbstractCacheManager,
        auth_manager: AbstractAuthManager,
        db_manager: AbstractDBManager,
    ) -> None:
        self._auth = auth_manager
        self._cache = cache_manager
        self._db = db_manager

    def get_file_path(
        self, index: int, user_session: UserSession
    ) -> str | None:
        if not self._auth.check_permissions(user_session=user_session):
            print("Ошибка - нет доступа в систему!")
            return None

        file_path = self._cache.get_file_path(index=index)
        if not file_path:
            file_path = self._db.get_file_path(
                index=index, user_session=user_session
            )
            if file_path:
                self._cache.add_file_path(index=index, path=file_path)

        return file_path

    def add_user(self, user_session: UserSession) -> None:
        if not self._auth.check_permissions(user_session=user_session):
            print("Ошибка - нет доступа в систему!")
            return None

        self._db.add_user(user_session=user_session)

    def add_file_path(
        self, index: int, path: str, user_session: UserSession
    ) -> None:
        if not self._auth.check_permissions(user_session=user_session):
            print("Ошибка - нет доступа в систему!")
            return None

        self._db.add_file_path(
            index=index, path=path, user_session=user_session
        )


test_mok_auth = MokAuthDatabase(users={}, permissions={})
test_mok_db = MokDatabase(paths={}, users={})
test_cache = {}

test_db_manager = BaseDBManager(mok_database=test_mok_db)
test_cache_manager = BaseCacheManager(mok_cache=test_cache)
test_auth_manager = BaseAuthManager(mok_auth=test_mok_auth)
test_proxy = DBManagerProxy(
    cache_manager=test_cache_manager,
    auth_manager=test_auth_manager,
    db_manager=test_db_manager,
)
