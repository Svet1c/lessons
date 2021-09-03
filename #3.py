# 3 задание

list_1 = [2, 3, 4]
list_2 = [5, 6, 7, 8, 9, 0]
while True:
    percent = int(input("Введите кол-во % : "))
    if percent % 10 == 1:
        print(percent, "процент")
    elif percent % 10 in list_1:
        print(percent, "процента")
    elif percent % 10 in list_2:
        print(percent, "процентов")