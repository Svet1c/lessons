# task 2 == done

class Zero_error(ZeroDivisionError):
    def __init__(self, text):
        self.text = text


if __name__ == "__main__":
    ipt = input('Enter number\n==>')
    try:
        ipt = int(ipt)
        if ipt == 0:
            raise Zero_error('Cannot be divided by zero!')
        else:
            print(f'100 / {ipt} =', 100/ipt)
    except ValueError:
        print(f'{ipt} is not number!')
    except Zero_error as f:
        print(f)
