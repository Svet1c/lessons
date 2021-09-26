# task 6

def show_sales_null():
    sale_list = []
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        for sale in f:
            sale_list.append(sale.strip())
        return sale_list[:]


def show_sales_arg1(start):
    sale_list = []
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        for sale in f:
            sale_list.append(sale.strip())
        return sale_list[start-1:]


def show_sales_arg2(arg):
    start = arg[:arg.find(" ")]
    end = arg[arg.find(' ')+1:]
    sale_list = []
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        for sale in f:
            sale_list.append(sale.strip())
        return sale_list[int(start)-1: int(end)]


if __name__ == '__main__':
    inp = input("enter start or start and end or nothing: ")
    if " " in inp:
        for i in show_sales_arg2(inp):
            print(i)
    elif len(inp) > 0:
        for i in show_sales_arg1(int(inp)):
            print(i)
    else:
        for i in show_sales_null():
            print(i)