# task 2 = done

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def formula(self):
        answer = int(self._length * self._width * 25 * 5 / 1000)
        return f'{self._length} м * {self._width} м * 25 кг * 5 см = {answer} т.'


if __name__ == "__main__":
    a = Road(int(input('enter length: ')), int(input('enter width: ')))
    print(a.formula())