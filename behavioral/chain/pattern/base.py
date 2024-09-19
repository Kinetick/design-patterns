from .abc import AbstractPassValidator


class PasswordValidationError(Exception):
    """Ошибка валидации пароля."""

    def __init__(self, message: str) -> None:
        self.message = message

    @classmethod
    def create_length_error(cls) -> "PasswordValidationError":
        """Фабричный метод создания ошибки длины пароля."""
        message = "Длина пароля менее 10 символов."
        return cls(message)

    @classmethod
    def create_only_alphabetical_error(cls) -> "PasswordValidationError":
        """Фабричный метод создания ошибки если в теле только буквы."""
        message = "В теле пароля не допускаются только буквы."
        return cls(message)

    @classmethod
    def create_only_numerical_error(cls) -> "PasswordValidationError":
        """Фабричный метод создания ошибки если в теле только цифры."""
        message = "В теле пароля не допускаются только цифры."
        return cls(message)

    @classmethod
    def create_only_special_error(cls) -> "PasswordValidationError":
        """Фабричный метод создания ошибки если в теле только спецсимволы."""
        message = "В теле пароля не допускаются только спецсимволы."
        return cls(message)

    @classmethod
    def create_not_special_error(cls) -> "PasswordValidationError":
        """Фабричный метод создания ошибки если в теле нет спецсимволов."""
        message = "В теле пароля должны присутствовать спецсимволы."
        return cls(message)

    @classmethod
    def create_not_alphabetical_error(cls) -> "PasswordValidationError":
        """Фабричный метод создания ошибки если в теле нет букв."""
        message = "В теле пароля должны присутствовать буквы."
        return cls(message)

    @classmethod
    def create_not_numerical_error(cls) -> "PasswordValidationError":
        """Фабричный метод создания ошибки если в теле нет цифр."""
        message = "В теле пароля должны присутствовать буквы."
        return cls(message)

    @classmethod
    def create_case_error(cls) -> "PasswordValidationError":
        """Фабричный метод создания ошибки если регистр только один."""
        message = (
            "В теле пароля должны присутствовать символы в разном регистре."
        )
        return cls(message)


class BasePassValidator(AbstractPassValidator):
    """Базовый валидатор пароля."""

    def __init__(
        self, validator: "AbstractPassValidator | None" = None
    ) -> None:
        self._next_validator = validator

    def set_next_validator(self, validator: "AbstractPassValidator") -> None:
        self._next_validator = validator

    def _validate(self, password: str) -> str:
        upper_password = password.upper()
        lower_password = password.casefold()
        if upper_password == password or lower_password == password:
            raise PasswordValidationError.create_case_error()

        return password

    def validate(self, password: str) -> str | None:
        validated_password = None
        try:
            validated_password = self._validate(password)
        except PasswordValidationError as e:
            print(f"Валидатор: {self} :: Ошибка: {e.message}")
        else:
            print(f"Валидатор: {self} :: ОК.")
            if self._next_validator is not None:
                validated_password = self._next_validator.validate(
                    validated_password
                )

        return validated_password

    def __str__(self) -> str:
        return self.__class__.__name__
