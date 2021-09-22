# task 5


def nums_not_repeat_list(list_of_num):
    result = []
    count = 0
    for num in list_of_num:
        if num not in list_of_num[count + 1:] and num not in list_of_num[:count]:
            result.append(num)
        count += 1
    return result


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

if __name__ == "__main__":
    print(nums_not_repeat_list(src))
