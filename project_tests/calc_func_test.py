from project_calc.calc_func import calculate
import pytest

@pytest.mark.parametrize("expression, expected_result", [
    ("2 + 2", 4),
    ("3 * 5", 15),
    ("10 / 2", 5),
    ("7 - 3", 4),
    ("2 ** 3", 8),
    ("1 / 0", "Некорректный ввод!"),
    ("abc", "Некорректный ввод!"),
    ("7", 7),
    ("31 - 0.0000005", 30.9999995)
])

def test_linear_search(expression, expected_result):
    assert calculate(expression) == expected_result
