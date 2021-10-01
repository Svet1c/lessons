# task 4
import os


def sort_files(path):
    f_list = []
    f_list_1000 = []
    f_list_10000 = []
    f_list_100000 = []
    m_list = []
    root_dir = path
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if os.stat(os.path.join(root, file)).st_size < 100:
                f_list.append(files)
            elif os.stat(os.path.join(root, file)).st_size < 1000:
                f_list_1000.append(file)
            elif os.stat(os.path.join(root, file)).st_size < 10000:
                f_list_10000.append(file)
            elif os.stat(os.path.join(root, file)).st_size < 100000:
                f_list_100000.append(file)
            else:
                m_list.append(file)
    for_print = {100: len(f_list), 1000: len(f_list_1000), 10000: len(f_list_10000), 100000: len(f_list_100000)}
    return for_print


if __name__ == '__main__':
    print(sort_files(input(r'enter path:')))