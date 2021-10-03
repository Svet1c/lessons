# task 3
from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args):
        result_list = ''
        for arg in args:
            if result_list:
                result_list += ', '
            result = type(arg)
            result_list += f'{func.__name__}({arg}: {result})'
        return result_list

    return wrapper


@type_logger
def calc_cube(*args):
    for arg in args:
        print(arg ** 3)


if __name__ == "__main__":
    print(calc_cube(2))