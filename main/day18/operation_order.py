import operator
import re


def solve(expression: str, addition_precedence: bool = False) -> int:
    if expression.count('(') > 0:
        closing_bracket_idx = expression.find(')')
        opening_bracket_idx = expression[:closing_bracket_idx].rfind('(')
        inner_equation = expression[opening_bracket_idx + 1:closing_bracket_idx]
        reduced = reduce_equation_precedence(inner_equation) if addition_precedence else reduce_equation_no_precedence(
            inner_equation)
        new_equation = expression[:opening_bracket_idx] + reduced + expression[closing_bracket_idx + 1:]
        return solve(new_equation, addition_precedence)

    return int(reduce_equation_precedence(expression) if addition_precedence else reduce_equation_no_precedence(
        expression))


def reduce_equation_no_precedence(inner_equation: str) -> str:
    if inner_equation.count(" ") > 0:
        return reduce_equation_no_precedence(perform_calculation(inner_equation))
    else:
        return str(inner_equation)


def reduce_equation_precedence(inner_equation: str) -> str:
    if inner_equation.count(" ") > 0:
        regex = list(re.finditer(r"(\d+) [+] (\d+)", inner_equation))
        if len(regex) == 0:
            return str(reduce_equation_precedence(perform_calculation(inner_equation)))
        else:
            start = regex[0].start()
            end = regex[0].end()
            ans = perform_calculation(inner_equation[start:end])
            reduced = inner_equation[:start] + ans + inner_equation[end:]
            return str(reduce_equation_precedence(reduced))
    else:
        return str(inner_equation)


def perform_calculation(equation: str) -> str:
    regex = re.search(r"^(\d*) ([*+]) (\d*)", equation)
    op = operator.mul if regex.group(2) == "*" else operator.add
    ans = op(int(regex.group(1)), int(regex.group(3)))
    return str(ans) + equation[regex.span(3)[1]:]
