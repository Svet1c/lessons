# task 1


def odd_nums(num):
    for number in range(1, num + 1, 2):
        yield number


if __name__ == "__main__":
    nums = odd_nums(15)
    print(next(nums))  # 1
    print(next(nums))  # 3
    print(next(nums))  # 5