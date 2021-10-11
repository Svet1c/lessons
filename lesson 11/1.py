# task 1 == done

class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def road_to_int(cls, param):
        fr = param.find('-')
        sc = param.find('-', fr + 1)
        return f'{int(param[:fr])} --> {type(int(param[sc+1:]))}\n' \
               f'{int(param[fr+1:sc])} --> {type(int(param[sc+1:]))}\n' \
               f'{int(param[sc+1:])} --> {type(int(param[sc+1:]))}'

    @staticmethod
    def valid_date(param):
        d31 = [1, 3, 5, 7, 8, 10, 12]
        d30 = [4, 6, 9, 11]
        fr, sc = param.find('-'),  param.find('-', param.find('-') + 1)
        if len(param[sc+1:]) == 4:
            if 0 < int(param[fr + 1: sc]) < 13:
                if int(param[fr + 1: sc]) in d31:
                    if 0 < int(param[:fr]) < 32:
                        return f"Valid {param}"
                    else:
                        return f'Not valid {param}'
                elif int(param[fr + 1: sc]) in d30:
                    if 0 < int(param[:fr]) < 31:
                        return f"Valid {param}"
                    else:
                        return f'Not valid {param}'
                elif int(param[fr + 1: sc]) == 2:
                    if int(param[sc+1:]) % 4 == 0:
                        if 0 < int(param[:fr]) < 30:
                            return f"Valid {param}"
                    elif 0 < int(param[:fr]) < 29:
                        return f"Valid {param}"
                    else:
                        return f'Not valid {param}'
                else:
                    return f'Not valid {param}'
            else:
                return f'Not valid {param}'
        else:
            return f'Not valid {param}'


if __name__ == "__main__":
    ipt = input('Enter date(dd:mm:yyyy)\n==>')
    a = Date(ipt)
    print(a.valid_date(ipt))
    print(a.road_to_int(ipt))