# 1+2

en_num = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
ru_num = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять']


def number_translate_upd(number):
    if number.lower() in en_num:
        if number.islower():
            idx = en_num.index(number)
            print(ru_num[idx])
        elif number.istitle():
            idx = en_num.index(number.lower())
            print(ru_num[idx].capitalize())
        else:
            print('None')
    else:
        print('None')


if __name__ == "__main__":
    num = input()
    number_translate_upd(num)

