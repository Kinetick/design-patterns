from typing import Type

from behavioral.interpreter.pattern import (
    ArithmeticExpression,
)

from .pattern import (
    AbstractArithmeticPrioritiesRepo,
    AddExpression,
    BracketExpression,
    DivExpression,
    MulExpression,
    NumericExpression,
    SubExpression,
)


class ArithmeticPrioritiesRepo(AbstractArithmeticPrioritiesRepo):
    """Реализация репозитория приоритета арифметических операций."""

    def register_level(
        self, level: dict[str, Type[ArithmeticExpression]]
    ) -> None:
        self._map_priorities[self.last_level_index] = level
        self.last_level_index += 1

    def get_level(self, index: int) -> dict[str, Type[ArithmeticExpression]]:
        return self._map_priorities[index]


def approximate_method(
    expression: list[str],
    priorities_repo: AbstractArithmeticPrioritiesRepo,
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
                left_terminal_expression = NumericExpression(
                    expression[token_index - 1]
                )
                right_terminal_expression = NumericExpression(
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
