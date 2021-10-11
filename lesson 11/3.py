# task 3 == done

class Int_list(ValueError):
    def __init__(self, txt):
        self.txt = txt


if __name__ == "__main__":
    ipt_list = []
    print('Enter number for list ("stop" for exit)')
    while True:
        ipt = input('==> ')
        try:
            if ipt.isdigit():
                ipt_list.append(int(ipt))
            elif ipt == 'stop':
                break
            else:
                raise Int_list(f'Wrong value: {ipt} is not number!')
        except Int_list as f:
            print(f)
    print(ipt_list)
