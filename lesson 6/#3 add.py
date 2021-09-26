# task 6

if __name__ == "__main__":
    with open('bakery.csv', 'a+', encoding='utf-8') as f:
        while True:
            inp = input('enter sale (s for stop):')
            if inp.isdigit():
                f.write(inp)
                f.write('\n')
            elif inp == "s":
                break