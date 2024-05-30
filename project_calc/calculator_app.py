class Calculator:
    def __init__(self):
        pass

    @staticmethod
    def validate_input(input_str):
        try:
            eval(input_str)  # Пытаемся вычислить введенное выражение
            return True
        except Exception:
            return False

    def calculate(self, expression):
        if not Calculator.validate_input(expression):
            return "Некорректный ввод!"

        try:
            result = eval(expression)
            return result
        except Exception as e:
            return f"Ошибка при вычислении: {e}"


def main():
    calc = Calculator()
    print("Для выхода введите 'exit'")
    while True:
        expression = input("Введите выражение: ")
        if expression.lower() == "exit":
            print("До свидания!")
            break

        result = calc.calculate(expression)
        print("Результат:", result)


if __name__ == "__main__":
    main()