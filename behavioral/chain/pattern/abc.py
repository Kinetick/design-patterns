from abc import ABC, abstractmethod


class AbstractPassValidator(ABC):
    """Абстрактный валидатор пароля."""

    @abstractmethod
    def set_next_validator(self, validator: "AbstractPassValidator") -> None:
        """Интерфейс установки следующего звена валидации."""
        ...

    @abstractmethod
    def _validate(self, password: str) -> str:
        """Интерфейс валидации пароля."""
        ...

    @abstractmethod
    def validate(self, password: str) -> str | None:
        """Интерфейс инициации валидации пароля."""
        ...
