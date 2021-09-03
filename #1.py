# 1 задание

while True:
    number = int(input("Введите число : "))
    sec = number
    if number >= 60:
        minutes = number // 60
        sec = number % 60
        if minutes >= 60:
            hours = minutes // 60
            minutes = minutes % 60
            if hours >= 24:
                days = hours // 24
                hours = hours % 24
                print(days, "дней,", hours, "часов,", minutes, "минут,", sec, "секунд")
                continue
            print(hours, "часов,", minutes, "минут,", sec, "секунд")
            continue
        print(minutes, "минут,", sec, "секунд")
        continue
    print(sec, "секунд")