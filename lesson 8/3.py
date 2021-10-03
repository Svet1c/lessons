# task 4
from functools import wraps


def callback(arg):
    if arg > 0:
        return 1
    else:
        return 0


def logger(call_back):
    @wraps(call_back)
    def _logger(func):
        def wrapper(args):
            if call_back(args) == 1:
                return f"{func(args)}"
            else:
                msg = f"Wrong val {args}"
                raise ValueError(msg)

        return wrapper

    return _logger


@logger(callback)
def cube_calc(x):
    return x ** 3


if __name__ == '__main__':
    print(cube_calc(3))