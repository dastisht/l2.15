import logging
import argparse

class NegativeIndexError(Exception):
    def __init__(self):
        super().__init__("Отрицательные индексы недопустимы")

def get_element(lst, index):
    if index < 0:
        logging.error("Попытка доступа к элементу с отрицательным индексом")
        raise NegativeIndexError()
    return lst[index]

def main():
    parser = argparse.ArgumentParser(description="Получение элемента списка по индексу")
    parser.add_argument("index", type=int, help="Индекс элемента")
    args = parser.parse_args()

    logging.basicConfig(level=logging.ERROR, format="%(levelname)s: %(message)s")

    try:
        my_list = [1, 2, 3, 4, 5]
        element = get_element(my_list, args.index)
        print("Выбранный элемент:", element)
    except NegativeIndexError as e:
        logging.error(e)
    except IndexError:
        logging.error("Индекс выходит за пределы списка")

if __name__ == "__main__":
    main()
