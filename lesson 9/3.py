# task 3 = done

class Worker:
    income_dict = {'wage': 100000, 'bonus': 15000}
    name = 'Авралий'
    surname = 'фавр'
    position = 'ген.директор'
    _income = income_dict


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income['wage'] = wage
        self._income['bonus'] = bonus

    def get_full_name(self):
        print(f'{self.name} {self.surname}')

    def get_total_income(self):
        wage = self._income['wage']
        bonus = self._income['bonus']
        print(wage + bonus)


if __name__ == '__main__':
    a = Position(input('Enter name: '), input('Enter surname: '), input('Enter position: '), int(input('Enter wage: ')),
                 int(input('Enter bonus: ')))
    a.get_full_name()
    a.get_total_income()