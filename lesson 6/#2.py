# task 3 + 4 + 5

def users_hobby_def(name_dir, hobby_dir, fin_dir):
    name_list = []
    hobby_list = []
    count = 0
    with open(name_dir, 'r', encoding='utf-8') as names:
        for name in names:
            name_list.append(name)
    with open(hobby_dir, 'r', encoding='utf-8') as hobbies:
        for hobby in hobbies:
            hobby_list.append(hobby)
    with open(fin_dir, 'a', encoding='utf-8') as users:
        try:
            for name in name_list:
                users.write(name[:-1] + ': ' + hobby_list[count])
                count += 1
        except IndexError:
            users.write(name[:-1] + ': ' + "None")
        try:
            if hobby_list[count] and not name_list[count]:
                users.write(name_list[count] + ': ' + hobby_list[count])
        except IndexError:
            print('Process finished with exit code 1')


if __name__ == "__main__":
    users_hobby_def(input('Введите имя файла с именами пользавателей: '),
                    input('Введите имя файла с хобби пользавателей: '),
                    input('Введите имя для нового файла(.txt): '))
