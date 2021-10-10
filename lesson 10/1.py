# task 1 == done


class Matrix:
    matrix = ''

    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists

    def __str__(self):
        for lists in self.list_of_lists:
            for i in lists:
                self.matrix += str(f'{i} ')
            self.matrix += str(f'\n')
        return self.matrix

    def __add__(self, other):
        new_matrix = ''
        sf_matrix = []
        ot_matrix = []
        for i in self.matrix:
            sf_matrix.append(i)
        for i in other.matrix:
            ot_matrix.append(i)
        for i in range(len(self.matrix)):
            if sf_matrix[i] == ' ':
                new_matrix += ' '
                continue
            elif sf_matrix[i] == '\n':
                new_matrix += '\n'
                continue
            new_matrix += str(int(ot_matrix[i]) + int(sf_matrix[i]))
        return new_matrix


l_of_l = [[2, 3, 4, 8], [5, 0, 6, 7]]
l_of_l2 = [[4, 5, 8, 5], [7, 5, 9, 3]]
if __name__ == '__main__':
    a = Matrix(l_of_l)
    b = Matrix(l_of_l2)
    print(a)
    print(b)
    print(a + b)