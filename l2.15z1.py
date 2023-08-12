import logging
import argparse

class DivisionByZeroError(Exception):
    def __init__(self):
        super().__init__("Деление на ноль недопустимо")

def divide(a, b):
    if b == 0:
        logging.error("Попытка деления на ноль")
        raise DivisionByZeroError()
    return a / b

def main():
    parser = argparse.ArgumentParser(description="Деление двух чисел")
    parser.add_argument("numerator", type=float, help="Числитель")
    parser.add_argument("denominator", type=float, help="Знаменатель")
    args = parser.parse_args()

    logging.basicConfig(level=logging.ERROR, format="%(levelname)s: %(message)s")

    try:
        result = divide(args.numerator, args.denominator)
        print("Результат деления:", result)
    except DivisionByZeroError as e:
        logging.error(e)

if __name__ == "__main__":
    main()
