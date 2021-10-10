# task 3 == done

class Cell:
    def __init__(self, quantity_of_cell, order):
        self.quantity_of_cell = quantity_of_cell
        self.order = order

    def __add__(self, other):
        return self.quantity_of_cell + other.quantity_of_cell

    def __sub__(self, other):
        if self.quantity_of_cell != other.quantity_of_cell:
            if self.quantity_of_cell > other.quantity_of_cell:
                return self.quantity_of_cell - other.quantity_of_cell
            else:
                return other.quantity_of_cell - self.quantity_of_cell
        else:
            return f'Между колличеством кдеток нет разницы!'

    def __mul__(self, other):
        return self.quantity_of_cell * other.quantity_of_cell

    def __floordiv__(self, other):
        if self.quantity_of_cell > other.quantity_of_cell:
            return self.quantity_of_cell // other.quantity_of_cell
        else:
            return other.quantity_of_cell // self.quantity_of_cell

    @property
    def make_order(self):
        count = 0
        return_ = ''
        for _ in range(self.quantity_of_cell):
            count += 1
            return_ += '[]'
            if count == self.order:
                return_ += '\n'
                count = 0
        return return_


if __name__ == "__main__":
    a = Cell(int(input()), int(input()))
    b = Cell(int(input()), int(input()))
    print(a + b)
    print(a - b)
    print(a * b)
    print(a // b)
    print(a.make_order)
    print(b.make_order)