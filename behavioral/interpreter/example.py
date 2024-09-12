from typing import Callable

from behavioral.interpreter.pattern import (
    BaseArithmeticExpression,
)

from .pattern import (
    AbstractExpression,
    BaseArithmeticPrioritiesRepo,
    BaseNumericExpression,
)


class BracketExpression(AbstractExpression):
    """Реализация интерпретации выражения скобок."""

    def __init__(
        self,
        expression: list[str],
        approximation_method: Callable[
            [list[str], BaseArithmeticPrioritiesRepo], list[str]
        ],
        arithmetic_priorities_repo: BaseArithmeticPrioritiesRepo,
    ):
        self._expression = expression
        self._approximation_method = approximation_method
        self._arithmetic_priorities_repo = arithmetic_priorities_repo

    def interpret(self) -> list[str]:
        self._expression = self._approximation_method(
            self._expression, self._arithmetic_priorities_repo
        )
        return self._expression


class AddExpression(BaseArithmeticExpression):
    """Реализация интерпретации выражения сложения."""

    def interpret(self) -> float:
        return (
            self._left_expression.interpret()
            + self._right_expression.interpret()
        )


class SubExpression(BaseArithmeticExpression):
    """Реализация интерпретации выражения вычитания."""

    def interpret(self) -> float:
        return (
            self._left_expression.interpret()
            - self._right_expression.interpret()
        )


class DivExpression(BaseArithmeticExpression):
    """Реализация интерпретации выражения деления."""

    def interpret(self) -> float:
        return (
            self._left_expression.interpret()
            / self._right_expression.interpret()
        )


class MulExpression(BaseArithmeticExpression):
    """Реализация интерпретации выражения умножения."""

    def interpret(self) -> float:
        return (
            self._left_expression.interpret()
            * self._right_expression.interpret()
        )


class ArithmeticPrioritiesRepo(BaseArithmeticPrioritiesRepo):
    """Реализация репозитория приоритета арифметических операций."""


def approximate_method(
    expression: list[str],
    priorities_repo: BaseArithmeticPrioritiesRepo,
) -> list[str]:
    """Метод ступенчатой аппроксимации на основе приоритета операций."""

    if not expression:
        return []

    if expression[0] == "(":
        expression = expression[1:]

    for priority_index in range(priorities_repo.last_level_index):
        token_index = 0
        priories_level = priorities_repo.get_level(priority_index)
        while token_index < len(expression):
            token = expression[token_index]
            if token in priories_level and expression[token_index + 1] != "(":
                arithmetic_expression = priories_level[token]
                left_terminal_expression = BaseNumericExpression(
                    expression[token_index - 1]
                )
                right_terminal_expression = BaseNumericExpression(
                    expression[token_index + 1]
                )
                approximal_token = arithmetic_expression(
                    left_terminal_expression,
                    right_terminal_expression,
                ).interpret()

                left_part_expression = expression[: token_index - 1]
                right_part_expression = expression[token_index + 2 :]
                left_part_expression.append(str(approximal_token))
                expression = left_part_expression + right_part_expression

            elif token == "(":
                left_part_expression = expression[:token_index]
                right_part_expression = BracketExpression(
                    expression[token_index:],
                    approximate_method,
                    priorities_repo,
                ).interpret()
                expression = left_part_expression + right_part_expression
                token_index -= 1

            elif token == ")":
                if priority_index == priorities_repo.last_level_index - 1:
                    left_part_expression = expression[:token_index]
                    right_part_expression = expression[token_index + 1 :]
                    expression = left_part_expression + right_part_expression
                break

            else:
                token_index += 1

    return expression


level_0 = {"*": MulExpression, "/": DivExpression}
level_1 = {"+": AddExpression, "-": SubExpression}
