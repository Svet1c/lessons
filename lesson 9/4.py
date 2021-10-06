# task 4 = done
import random

turn_list = ['лево', 'право']


class Car:
    speed = 0
    color = ''
    name = ''
    is_police = False

    def go(self):
        return f'Машина {self.name} поехала!'

    def stop(self):
        return f'Машина {self.name} останвилась!'

    def turn(self):
        turn = random.choice(turn_list)
        return f'Машина {self.name} повернула на {turn}!'

    def show_speed(self):
        return self.speed


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        self.speed, self.color, self.name, self.is_police = speed, color, name, is_police

    def show_speed(self):
        if self.speed > 60:
            return f'{self.speed} Вы превышаете!'
        else:
            return self.speed


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        self.speed, self.color, self.name, self.is_police = speed, color, name, is_police


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        self.speed, self.color, self.name, self.is_police = speed, color, name, is_police

    def show_speed(self):
        if self.speed > 40:
            return f'{self.speed} Вы превышаете!'
        else:
            return self.speed


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        self.speed, self.color, self.name, self.is_police = speed, color, name, is_police


if __name__ == "__main__":
    t = TownCar(50, 'purple', 'lada Largus', False)
    s = SportCar(120, 'red', 'Lamborghini', False)
    w = WorkCar(40, 'orange', 'KAMAZ', False)
    p = PoliceCar(80, 'white', 'lada Calina', True)
    print(t.name, t.color, t.is_police, t.go(), t.turn(), t.show_speed(), t.stop())
    print(s.name, s.color, s.is_police, s.go(), s.turn(), s.show_speed(), s.stop())
    print(w.name, w.color, w.is_police, w.go(), w.turn(), w.show_speed(), w.stop())
    print(p.name, p.color, p.is_police, p.go(), p.turn(), p.show_speed(), p.stop())