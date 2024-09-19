from ..pattern.base import (
    BaseApproximate,
    BaseArithmeticExpression,
    BaseArithmeticPrioritiesRepo,
    BaseBracketExpression,
)


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


test_interpret_tokens = list(
    map(str, "1 + 2 * 4 * (  ( 1 + 2 ) * 5 ) / 2".split())
)

level_0 = {"*": MulExpression, "/": DivExpression}
level_1 = {"+": AddExpression, "-": SubExpression}

common_priorities = BaseArithmeticPrioritiesRepo()
common_priorities.register_level(level=level_0)
common_priorities.register_level(level=level_1)
common_approximator = BaseApproximate(
    priorities_repo=common_priorities, bracket_expression=BaseBracketExpression
)

test_result = BaseBracketExpression(
    interpret_tokens=test_interpret_tokens, approximator=common_approximator
).interpret()
