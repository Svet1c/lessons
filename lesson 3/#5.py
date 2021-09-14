# 5 'я не нашел способа сделать так, чтобы слова не повторялись ;('

import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def joke(num):
    """ Выбор слов для шутки """
    while num:
        jk = [random.choice(nouns), random.choice(adverbs), random.choice(adjectives)]
        print(" ".join(jk))
        num -= 1


if __name__ == "__main__":
    jokes_num = int(input())
    joke(jokes_num)
