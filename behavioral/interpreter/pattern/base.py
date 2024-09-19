from typing import Type, TypeAlias

from .abc import (
    AbstractApproximation,
    AbstractArithmeticPrioritiesRepo,
    AbstractExpression,
)

ARITHMETIC_LEVELS: TypeAlias = dict[str, Type["BaseArithmeticExpression"]]


class BaseNumericExpression(AbstractExpression):
    """Базовый класс терминального выражения (числа)."""

    def __init__(self, expression: str) -> None:
        self._expression = expression

    def interpret(self):
        return float(self._expression)


class BaseArithmeticExpression(AbstractExpression):
    """Базовый класс нетерминального выражения (ариф. операция)."""

    def __init__(
        self,
        left_expression: BaseNumericExpression,
        right_expression: BaseNumericExpression,
    ) -> None:
        self._left_expression = left_expression
        self._right_expression = right_expression


class BaseArithmeticPrioritiesRepo(AbstractArithmeticPrioritiesRepo):
    """Базовый класс репозитория приоритетов операций."""

    def __init__(
        self,
    ) -> None:
        self._map_prior: dict[int, ARITHMETIC_LEVELS] = {}
        self._last_level_index = 0

    @property
    def last_index(self) -> int:
        return self._last_level_index

    def register_level(self, level: ARITHMETIC_LEVELS) -> None:
        self._map_prior[self._last_level_index] = level
        self._last_level_index += 1

    def get_level(self, index: int) -> ARITHMETIC_LEVELS:
        return self._map_prior[index]


class BaseBracketExpression(AbstractExpression):
    """Базовый класс выражения скобок."""

    def __init__(
        self, interpret_tokens: list[str], approximator: AbstractApproximation
    ):
        self._tokens = interpret_tokens
        self._approximator = approximator

    def interpret(self) -> list[str]:
        self._tokens = self._approximator.approximate(
            interpret_tokens=self._tokens
        )

        return self._tokens


class BaseApproximate(AbstractApproximation):
    def __init__(
        self,
        priorities_repo: AbstractArithmeticPrioritiesRepo,
        bracket_expression: Type[BaseBracketExpression],
    ) -> None:
        self._priorities = priorities_repo
        self._brackets = bracket_expression

    def _build_brackets(
        self, interpret_tokens: list[str]
    ) -> BaseBracketExpression:
        """Фабричный метод создания выражения скобок."""

        return BaseBracketExpression(
            interpret_tokens=interpret_tokens, approximator=self
        )

    def approximate(self, interpret_tokens: list[str]) -> list[str]:
        if not interpret_tokens:
            return []

        if interpret_tokens[0] == "(":
            interpret_tokens = interpret_tokens[1:]

        for priority_index in range(self._priorities.last_index):
            token_index = 0
            priories_level = self._priorities.get_level(priority_index)

            while token_index < len(interpret_tokens):
                token = interpret_tokens[token_index]
                if (
                    token in priories_level
                    and interpret_tokens[token_index + 1] != "("
                ):
                    arithmetic_expression = priories_level[token]
                    l_term_expression = BaseNumericExpression(
                        interpret_tokens[token_index - 1]
                    )
                    r_term_expression = BaseNumericExpression(
                        interpret_tokens[token_index + 1]
                    )
                    approximal_token = arithmetic_expression(
                        l_term_expression,
                        r_term_expression,
                    ).interpret()

                    l_part_tokens = interpret_tokens[: token_index - 1]
                    l_part_tokens.append(str(approximal_token))
                    r_part_tokens = interpret_tokens[token_index + 2 :]
                    interpret_tokens = l_part_tokens + r_part_tokens

                elif token == "(":
                    l_part_tokens = interpret_tokens[:token_index]
                    r_part_tokens = self._build_brackets(
                        interpret_tokens=interpret_tokens[token_index:]
                    ).interpret()
                    interpret_tokens = l_part_tokens + r_part_tokens
                    token_index -= 1

                elif token == ")":
                    if priority_index == self._priorities.last_index - 1:
                        l_part_tokens = interpret_tokens[:token_index]
                        r_part_tokens = interpret_tokens[token_index + 1 :]
                        interpret_tokens = l_part_tokens + r_part_tokens
                    break

                else:
                    token_index += 1

        return interpret_tokens
