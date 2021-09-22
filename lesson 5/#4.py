# task 4


def num_sequence(list_of_nums):
    result = []
    num2 = list_of_nums[0]
    for num in list_of_nums:
        if num > num2:
            result.append(num)
        num2 = num
    return result


src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123]


if __name__ == "__main__":
    print(num_sequence(src))