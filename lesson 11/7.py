# task 7 == done


class Complex_number:
    def __init__(self, num1, num2):
        self.comp_num = complex(num1, num2)

    def __add__(self, other):
        return self.comp_num + other.comp_num

    def __mul__(self, other):
        return self.comp_num * other.comp_num


if __name__ == '__main__':
    a = Complex_number(5, 8)
    b = Complex_number(3, 2)
    print(a + b)
    print(a * b)