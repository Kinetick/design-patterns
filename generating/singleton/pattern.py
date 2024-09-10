from functools import wraps
from threading import Lock
from typing import Any, Callable, ParamSpec, TypeVar


class NewMethodSingleton:
    """Реализация паттерна через перегрузку метода __new__."""

    _INSTANCE = None

    def __new__(cls, *args, **kwargs) -> "NewMethodSingleton":
        if cls._INSTANCE is None:
            cls._INSTANCE = super().__new__(cls, *args, **kwargs)

        return cls._INSTANCE


class MetaClassSingleton(type):
    """Реализация паттерна через метакласс."""

    _INSTANCES = {}

    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        instance = cls._INSTANCES.get(cls)
        if instance is None:
            instance = super().__call__(*args, **kwargs)
            cls._INSTANCES[cls] = instance

        return instance


PM = ParamSpec("PM")
RT = TypeVar("RT")
lock = Lock()


def with_lock(
    lock: Lock,
) -> Callable[[Callable[PM, RT]], Callable[PM, RT]]:
    """Синхронизатор для потокобезопасного вызова функции."""

    def decorator(f: Callable[PM, RT]) -> Callable[PM, RT]:
        @wraps(f)
        def args_wrap(*args: PM.args, **kwargs: PM.kwargs) -> RT:
            with lock:
                return f(*args, **kwargs)

        return args_wrap

    return decorator


class ThreadSafeSingleton(type):
    """Реализация 'thread safe' одиночки через метакласс."""

    _INSTANCES = {}

    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        instance = cls._INSTANCES.get(cls)
        if instance is None:
            instance = cls._locked_call(*args, **kwargs)

        return instance

    @with_lock(lock=lock)
    def _locked_call(cls, *args, **kwargs) -> Any:
        if cls not in cls._INSTANCES:
            instance = super(ThreadSafeSingleton, cls).__call__(
                *args, **kwargs
            )
            cls._INSTANCES[cls] = instance

        return instance


def singleton(cls):
    """Реализация паттерна через декоратор класса."""
    instances = {}

    @wraps(cls)
    def inner_wraps(*args, **kwargs):
        instance = instances.get(cls)
        if instance is None:
            instance = cls(*args, **kwargs)
            instances[cls] = instance
        return instance

    return inner_wraps
