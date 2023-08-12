import logging
import argparse

class NegativeRectangleSizeError(Exception):
    def __init__(self):
        super().__init__("Отрицательные размеры прямоугольника недопустимы")

def calculate_rectangle_area(length, width):
    if length < 0 or width < 0:
        logging.error("Попытка создания прямоугольника с отрицательной длиной или шириной")
        raise NegativeRectangleSizeError()
    return length * width

def main():
    parser = argparse.ArgumentParser(description="Вычисление площади прямоугольника")
    parser.add_argument("length", type=float, help="Длина прямоугольника")
    parser.add_argument("width", type=float, help="Ширина прямоугольника")
    args = parser.parse_args()

    logging.basicConfig(level=logging.ERROR, format="%(levelname)s: %(message)s")

    try:
        area = calculate_rectangle_area(args.length, args.width)
        print("Площадь прямоугольника:", area)
    except NegativeRectangleSizeError as e:
        logging.error(e)

if __name__ == "__main__":
    main()
