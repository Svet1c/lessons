# 3


def thesaurus(*args):
    name_sort = {}
    for name in args:
        name_list = []
        name_list.clear()
        name_list.append(name)
        if name[0] in name_sort:
            name_list = (name_sort.get(name[0])) + name_list
        name_sort[name[0]] = name_list
    print(name_sort)


if __name__ == "__main__":
    thesaurus("Иван", "Мария", "Петр", "Илья", "Анна", "Инна", "Анфиса")

