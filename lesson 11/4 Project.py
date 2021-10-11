# task 4, 5, 6 == done

class Wrong_value(ValueError):
    def __init__(self, txt):
        self.txt = txt


class Warehouse:
    office_equipment = {'printer': 0, 'scanner': 0, 'copier': 0}


class Office_equipment:
    def __init__(self, name):
        self.name = name


class Printer(Office_equipment):
    def __init__(self, number, name):
        super().__init__(name)
        self.number_of_printer = number

    def input(self):
        Warehouse.office_equipment[self.name] += self.number_of_printer

    def output(self):
        Warehouse.office_equipment[self.name] -= self.number_of_printer


class Scanner(Office_equipment):
    def __init__(self, number, name):
        super().__init__(name)
        self.number_of_scanner = number

    def input(self):
        Warehouse.office_equipment[self.name] += self.number_of_scanner

    def output(self):
        Warehouse.office_equipment[self.name] -= self.number_of_scanner


class Copier(Office_equipment):
    def __init__(self, number, name):
        super().__init__(name)
        self.number_of_copier = number

    def input(self):
        Warehouse.office_equipment[self.name] += self.number_of_copier

    def output(self):
        Warehouse.office_equipment[self.name] -= self.number_of_copier


if __name__ == "__main__":

    while True:
        ipt = input('\np --> printer || s --> scanner || c --> copier\nshow --> show warehouse || stop --> exit\n==> ')
        if ipt == 'p':
            while True:
                ipt_p = input('\nin --> +printer in warehouse\nout --> -printer in warehouse\nback --> for back\n==> ')
                if ipt_p == "in":
                    ipt = input('\nEnter number of printers\n==> ')
                    try:
                        if ipt.isdigit():
                            p = Printer(int(), "printer")
                            p.input()
                        else:
                            raise Wrong_value(f'{ipt} is not number')
                    except Wrong_value as f:
                        print(f)
                elif ipt_p == 'out':
                    ipt = input('\nEnter number of printers\n==> ')
                    try:
                        if ipt.isdigit():
                            p = Printer(int(), "printer")
                            p.output()
                        else:
                            raise Wrong_value(f'{ipt} is not number')
                    except Wrong_value as f:
                        print(f)
                elif ipt_p == 'back':
                    break
        elif ipt == 's':
            while True:
                ipt_s = input('\nin --> +scanner in warehouse\nout --> -scanner in warehouse\nback --> for back\n==> ')
                if ipt_s == "in":
                    ipt = input('\nEnter number of scanners\n==> ')
                    try:
                        if ipt.isdigit():
                            p = Scanner(int(), "scanner")
                            p.input()
                        else:
                            raise Wrong_value(f'{ipt} is not number')
                    except Wrong_value as f:
                        print(f)
                elif ipt_s == 'out':
                    ipt = input('\nEnter number of scanners\n==> ')
                    try:
                        if ipt.isdigit():
                            p = Scanner(int(), "scanner")
                            p.output()
                        else:
                            raise Wrong_value(f'{ipt} is not number')
                    except Wrong_value as f:
                        print(f)
                elif ipt_s == 'back':
                    break
        elif ipt == 'c':
            while True:
                ipt_p = input('\nin --> +copier in warehouse\nout --> -copier in warehouse\nback --> for back\n==> ')
                if ipt_p == "in":
                    ipt = input('\nEnter number of copiers\n==> ')
                    try:
                        if ipt.isdigit():
                            p = Copier(int(), "copier")
                            p.input()
                        else:
                            raise Wrong_value(f'{ipt} is not number')
                    except Wrong_value as f:
                        print(f)
                elif ipt_p == 'out':
                    ipt = input('\nEnter number of copiers\n==> ')
                    try:
                        if ipt.isdigit():
                            p = Copier(int(), "copier")
                            p.output()
                        else:
                            raise Wrong_value(f'{ipt} is not number')
                    except Wrong_value as f:
                        print(f)
                elif ipt_p == 'back':
                    break
        elif ipt == 'show':
            w = Warehouse()
            print(w.office_equipment)
        elif ipt == 'stop':
            break
