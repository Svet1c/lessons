# task 5 = done


class Stationary:
    title = ''

    def draw(self):
        return f'Запуск отрисовки!'


class Pen(Stationary):
    def draw(self):
        return f'Ручка: Запуск отрисовки!'


class Pencil(Stationary):
    def draw(self):
        return f'Карандаш: Запуск отрисовки!'


class Handle(Stationary):
    def draw(self):
        return f'Маркер: Запуск отрисовки!'


if __name__ == "__main__":
    s = Stationary()
    p = Pen()
    pc = Pencil()
    h = Handle()
    print(s.draw(), p.draw(), pc.draw(), h.draw(), sep='\n')