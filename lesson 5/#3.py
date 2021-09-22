# task 3


def students(list1, list2):
    count = 0
    while not count >= len(list1) or not count >= len(list2):
        if count < len(list1):
            name = list1[count]
        else:
            name = "None"
        if count < len(list2):
            klass = list2[count]
        else:
            klass = "None"
        student = (name, klass)
        yield student
        count += 1


tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
classes = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]


if __name__ == "__main__":
    std = students(tutors, classes)
    print(type(std))
    print(next(std))
    print(next(std))
    print(next(std))
    print(next(std))
    print(next(std))
    print(next(std))
    print(next(std))
    print(next(std))
    print(next(std))
    print(next(std))