import re

from ..pattern.base import (
    BasePassValidator,
    PasswordValidationError,
)


class PassLengthValidator(BasePassValidator):
    """Валидатор длины пароля."""

    def _validate(self, password: str) -> str:
        """Валидация длины пароля."""
        if len(password) < 10:
            raise PasswordValidationError.create_length_error()

        return password


class PassOnlyAlphabeticalValidator(BasePassValidator):
    """Валидатор наличия только букв в теле пароля."""

    def _validate(self, password: str) -> str:
        "Валидация на наличие только букв в теле пароля."
        if password.isalpha():
            raise PasswordValidationError.create_only_alphabetical_error()

        return password


class PassOnlyNumericalValidator(BasePassValidator):
    """Валидатор наличия только цифр в теле пароля."""

    def _validate(self, password: str) -> str:
        """Валидация на наличие только цифр в теле пароля."""
        if password.isnumeric():
            raise PasswordValidationError.create_only_numerical_error()

        return password


class PassOnlySpecialValidator(BasePassValidator):
    """Валидатор наличия только спецсимволов в теле пароля."""

    def _validate(self, password: str) -> str:
        """Валидация на наличие только спецсимволов в теле пароля."""
        special_pattern = re.compile(r"[#.\\|/@!#$]+")
        special_substring = special_pattern.search(password)
        if special_substring is not None:
            special_substring = special_substring.group()
            if len(special_substring) == len(password):
                raise PasswordValidationError.create_only_special_error()

        return password


class PassNotAlphabeticalValidator(BasePassValidator):
    """Валидатор отсутствия букв в теле пароля."""

    def _validate(self, password: str) -> str:
        """Валидация на отсутствие букв в теле пароля."""
        alphabetical_pattern = re.compile(r"[a-zA-Z]+")
        alphabetical_substring = alphabetical_pattern.search(password)
        if alphabetical_substring is None:
            raise PasswordValidationError.create_not_alphabetical_error()

        return password


class PassNotNumericalValidator(BasePassValidator):
    """Валидатор отсутствия цифр в теле пароля."""

    def _validate(self, password: str) -> str:
        """Валидация на отсутствие цифр в теле пароля."""
        numerical_pattern = re.compile(r"[0-9]+")
        numerical_substring = numerical_pattern.search(password)
        if numerical_substring is None:
            raise PasswordValidationError.create_not_numerical_error()

        return password


class PassNotSpecialValidator(BasePassValidator):
    """Валидатор отсутствия спецсимволов в теле пароля."""

    def _validate(self, password: str) -> str:
        """Валидация на отсутствие спецсимволов в теле пароля."""
        special_pattern = re.compile(r"[#.\\|/@!#$]+")
        special_substring = special_pattern.search(password)
        if special_substring is None:
            raise PasswordValidationError.create_not_special_error()

        return password


class PassCaseValidator(BasePassValidator):
    """Валидатор регистров тела пароля."""

    def _validate(self, password: str) -> str:
        """Валидация наличия разных регистров в теле пароля."""
        upper_password = password.upper()
        lower_password = password.casefold()
        if upper_password == password or lower_password == password:
            raise PasswordValidationError.create_case_error()

        return password


# * Здесь прямо напрашивается использование паттерна строитель.
pass_validator = PassLengthValidator()
pass_validator.set_next_validator(validator=PassOnlyAlphabeticalValidator())
pass_validator.set_next_validator(validator=PassOnlyNumericalValidator())
pass_validator.set_next_validator(validator=PassOnlySpecialValidator())
pass_validator.set_next_validator(validator=PassNotAlphabeticalValidator())
pass_validator.set_next_validator(validator=PassNotNumericalValidator())
pass_validator.set_next_validator(validator=PassNotSpecialValidator())
pass_validator.set_next_validator(validator=PassCaseValidator())
