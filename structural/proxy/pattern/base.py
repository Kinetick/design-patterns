from random import uniform
from time import sleep
from typing import TypedDict

from .abc import (
    AbstractAuthManager,
    AbstractCacheManager,
    AbstractDBManager,
)


class UserSession(TypedDict):
    """Модель пользовательской сессии."""

    login: str
    password: str


class UserAuthData(UserSession):
    """Модель данных авторизации пользователя"""

    permissions_mask: int


class MokAuthDatabase(TypedDict):
    """Мок БД сервиса авторизации."""

    users: dict[str, UserAuthData]
    permissions: dict[int, bool]


class MokDatabase(TypedDict):
    """Мок БД основного объекта."""

    paths: dict[int, str]
    users: dict[str, UserSession]


class BaseDBManager(AbstractDBManager):
    """Базовый класс менеджера БД."""

    def __init__(self, mok_database: MokDatabase) -> None:
        self._database = mok_database

    def get_file_path(
        self, index: int, user_session: UserSession
    ) -> str | None:
        user_key = str(hash(user_session['login'] + user_session['password']))
        is_current_user = bool(self._database['users'].get(user_key))
        if not is_current_user:
            print("Ошибка - пользователь не найден в СУБД.")
            return None

        sleep(uniform(0.5, 2))
        return self._database['paths'].get(index)

    def add_user(self, user_session: UserSession) -> None:
        if not (user_session['login'] and user_session['password']):
            print("Длины полей пароля и логина должны быть больше 0!")
            return None

        user_key = str(hash(user_session['login'] + user_session['password']))
        self._database['users'][user_key] = user_session

    def add_file_path(
        self, index: int, path: str, user_session: UserSession
    ) -> None:
        user_key = str(hash(user_session['login'] + user_session['password']))
        is_current_user = bool(self._database['users'].get(user_key))
        if not is_current_user:
            print("Ошибка - пользователь не найден в СУБД.")
            return None

        if index in self._database['paths']:
            print(f"Путь к файлу с индексом {index} уже есть в системе!")
            return None

        self._database['paths'][index] = path


class BaseCacheManager(AbstractCacheManager):
    """Базовый класс менеджера кеша."""

    def __init__(self, mok_cache: dict[int, str]) -> None:
        self._cache = mok_cache

    def get_file_path(self, index: int) -> str | None:
        return self._cache.get(index)

    def add_file_path(self, index: int, path: str) -> None:
        self._cache[index] = path


class BaseAuthManager(AbstractAuthManager):
    """Базовый класс менеджера авторизации."""

    def __init__(self, mok_auth: MokAuthDatabase) -> None:
        self._auth_db = mok_auth

    def check_permissions(self, user_session: UserSession) -> bool:
        user_key = str(hash(user_session['login'] + user_session['password']))
        user_data = self._auth_db['users'][user_key]
        permissions = bool(
            self._auth_db['permissions'].get(user_data['permissions_mask'])
        )

        return permissions

    def add_user(
        self, user_session: UserSession, permissions_mask: int
    ) -> None:
        if not (user_session['login'] and user_session['password']):
            print("Длины полей пароля и логина должны быть больше 0!")
            return None

        user_key = str(hash(user_session['login'] + user_session['password']))
        if user_key in self._auth_db['users']:
            print("Пользователь уже добавлен в систему.")
            return None

        if permissions_mask not in self._auth_db['permissions']:
            print("Привилегии не найдены в системе.")
            return None

        self._auth_db['users'][user_key] = UserAuthData(
            login=user_session['login'],
            password=user_session['password'],
            permissions_mask=permissions_mask,
        )

    def add_permissions(self, permissions_map: dict[int, bool]) -> None:
        for mask, permission in permissions_map.items():
            if mask in self._auth_db['permissions']:
                print(
                    (
                        f"Маска '{mask}' уже есть в системе и буден"
                        f"  перезаписана на '{permission}'!"
                    )
                )

                self._auth_db['permissions'][mask] = permission
