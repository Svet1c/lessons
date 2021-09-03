# 2 задание

number_list = []
for i in range(1000):
    if i % 2 != 0:
        i = i ** 3
        number_list.append(i)

# a

list_a = []
sum_of_number = 0
for i in number_list:
    p = 0
    for o in str(i):
        p += int(o)
    if p % 7 == 0:
        list_a.append(i)
        sum_of_number += i
print(sum_of_number)

# b + c

sum_of_number_b = 0
for i in list_a:
    i += 17
    p = 0
    for o in str(i):
        p += int(o)
        print(p)
    if p % 7 == 0:
        sum_of_number_b += i
print(sum_of_number_b)
