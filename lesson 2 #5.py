# задание 5 урок 2
# A
prices = [36.49, 63.05, 21.33, 49.63, 74.15, 19.08, 8.20, 88.05, 61.76, 95.16]
price_list = []
for price in prices:
    kop = str(int((price % 1).__round__(2)*100))
    rub = str(int(price // 1))
    if len(kop) < 2:
        price_list.append(rub + ' руб. ' + '0' + kop + ' коп.')
    else:
        price_list.append(rub + ' руб. ' + kop + ' коп.')
print("A")
print(','.join(price_list))

# B
print('B')
print(id(prices), prices)
prices.sort()
print(id(prices), prices)

# C
print('C')
prices_2 = [36.49, 63.05, 21.33, 49.63, 74.15, 19.08, 8.20, 88.05, 61.76, 95.16]
prices_2.sort(reverse=True)
print(prices_2)

# D
print("D")
print(prices_2[:5])