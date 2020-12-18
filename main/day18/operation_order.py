import operator
import re


def solve(expression: str) -> int:
    if expression.count('(') > 0:
        closing_bracket_idx = expression.find(')')
        opening_bracket_idx = expression[:closing_bracket_idx].rfind('(')
        inner_equation = expression[opening_bracket_idx + 1:closing_bracket_idx]
        reduced = reduce_equation(inner_equation)
        new_equation = expression[:opening_bracket_idx] + reduced + expression[closing_bracket_idx + 1:]
        return solve(new_equation)

    return int(reduce_equation(expression))


def reduce_equation(inner_equation: str) -> str:
    if inner_equation.count(" ") > 0:
        regex = re.search(r"^(\d*) ([*+]) (\d*)", inner_equation)
        lhs = int(regex.group(1))
        op = operator.mul if regex.group(2) == "*" else operator.add
        rhs = int(regex.group(3))
        ans = op(lhs, rhs)
        end_idx = regex.span(3)[1]
        reduced = str(ans) + inner_equation[end_idx:]
        return reduce_equation(reduced)
    else:
        return str(inner_equation)
