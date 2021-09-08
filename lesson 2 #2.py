# задание 2 урок 2

text = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
text_2 = []
for word in text:
    if word.isalpha():
        text_2.append(word)
        continue
    if word.isdigit:
        text_2.append('"')
        if word[0] == '+' or word[0] == '-':
            sign, char = word[0], word[1:]
            word = sign + '0' + char
            text_2.append(word)
        elif len(word) < 2:
            text_2.append('0' + word)
        else:
            text_2.append(word)
        text_2.append('"')
        continue
    continue
text = ' '.join(text_2)
print(text)
