from project_calc.calculator_app import Calculator


def calculate(expression):
    if not Calculator.validate_input(expression):
        return "Некорректный ввод!"

    try:
        result = eval(expression)
        return result
    except Exception as e:
        return f"Ошибка при вычислении: {e}"
