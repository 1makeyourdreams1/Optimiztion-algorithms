def gcd(a, b):
    if a == 0 or b == 0:
        return max(a, b)
    else:
        if a > b:
            return gcd(a - b, b)
        else:
            return gcd(a, b - a)


def simplex_method(matrix, cj, cb):
    max_elem = 0
    sign = 0
    for i in matrix[2]:
        sign = 0 if i > 0 else 1
        max_elem = max(abs(i), max_elem)
    max_elem = max_elem if sign == 0 else -max_elem
    # print(max_elem)
    inc = matrix[2].index(max_elem)
    # exc = 0 if matrix[0][4] / matrix[0][inc] < matrix[1][4] / matrix[1][inc] else 1
    exc = 0 if matrix[0][3] / matrix[0][inc] < matrix[1][3] / matrix[1][inc] else 1
    # new_matrix = [
    #     ["0", "0", "0", "0", "0"],
    #     ["0", "0", "0", "0", "0"],
    #     ["0", "0", "0", "0", "0"],
    # ]
    new_matrix = [
        ["0", "0", "0", "0"],
        ["0", "0", "0", "0"],
        ["0", "0", "0", "0"],
    ]
    ars = matrix[exc][inc]
    new_matrix[exc][inc] = round(1 / ars, 2)
    # print(matrix[exc][inc], new_matrix[exc][inc])
    for i in range(len(matrix[exc])):
        if i == inc:
            continue
        # nod = gcd(matrix[exc][i], ars)
        new_matrix[exc][i] = round(matrix[exc][i] / ars, 2)

    for j in range(len(matrix)):
        if j == exc:
            continue
        # nod = gcd(abs(matrix[j][inc]), ars)
        new_matrix[j][inc] = round(-matrix[j][inc] / ars, 2)

    for i in range(len(matrix)):
        if i == exc:
            continue
        for j in range(len(matrix[i])):
            if j == inc or i == 2 and j == 3: # j == 4
                continue
            # nod = gcd(abs(matrix[i][j] * ars - matrix[i][inc] * matrix[exc][j]), ars)
            new_matrix[i][j] = round((matrix[i][j] * ars - matrix[i][inc] * matrix[exc][j]) / ars, 2)
    result = 0
    for i in range(len(new_matrix) - 1):
        if i == exc:
            # params = list(map(int, new_matrix[i][4].split('/')))
            # result += cj[inc] * new_matrix[i][4]
            result += cj[inc] * new_matrix[i][3]
        else:
            # params = list(map(int, new_matrix[i][4].split('/')))
            # result += cb[i] * new_matrix[i][4]
            result += cb[i] * new_matrix[i][3]
    # new_matrix[2][4] = round(result, 2)
    new_matrix[2][3] = round(result, 2)
    cj[inc], cb[exc] = cb[exc], cj[inc]
    return (new_matrix, ars, inc, exc, cb, cj)


def print_matrix(matrix, ars, inc, exc, cb, cj):
    print(matrix)
    print(f"Разрешающий элемент: a{exc + 1}{inc + 1} = {ars}")
    print("Коэфф. целевой ф-и, соответствующие небазисным переменным: ", end='')
    for i in cj:
        print(i, end=' ')
    print("\nКоэфф. целевой ф-и, соответствующие базисным переменным: ", end='')
    for i in cb:
        print(i, end=' ')
    print()
    print('%-10s' % "", end='')
    for i in range(len(matrix[0]) - 1):
        if i == inc:
            print('%-10s' % ("X" + str(exc + 4)), end='')
        else:
            print('%-10s' % ("X" + str(i + 1)), end='')

    print('%-10s' % "A0", end='')
    print()
    n = 4
    for item in matrix:
        if n == 6:
            print('%-10s' % "f", end='')
        elif n == exc + 4:
            print('%-10s' % ("X" + str(inc + 1)), end='')
        else:
            print('%-10s' % ("X" + str(n)), end='')
        n += 1
        for c in item:
            print('%-10s' % str(c), end='')
        print()


def get_optimal_plan():
    matrix = [
        [3.5, 7, 4.2, 1400],
        [4, 5, 8, 2000],
        [-1, -3, -3]
    ]
    cj = [1, 3, 3]
    cb = [0, 0]
    # print("Итеряция 1")
    # print_matrix(*simplex_method(matrix, cj, cb))

    matrix = [[0.5, 0.14, 0.6, 200.0], [1.5, -0.71, 5.0, 1000.0], [0.5, 0.43, -1.2]]
    cj = [1, 0, 3]
    cb = [3, 0]
    # print("Итеряция 2")
    # print_matrix(*simplex_method(matrix, cj, cb))
    return int(simplex_method(matrix, cj, cb)[0][-1][-1])


# matrix = [
#     ["1/2", "3/2", "2/1", "3/2", "1200/1"],
#     ["4/1", "2/1", "6/1", "8/1", "1000/1"],
#     ["-5/1", "-5/1", "-25/2", "-10/1"]
# ]


# matrix = [
#     [0.5, 1.5, 2, 1.5, 1200],
#     [4, 2, 6, 8, 1000],
#     [-5, -5, -12.5, -10]
# ]
# cj = [5, 5, 12.5, 10]
# cb = [0, 0]
# print("Итеряция 1")
# print_matrix(*simplex_method(matrix, cj, cb))

# matrix = [
#     [-0.83, 0.83, -0.33, -1.17, 866.67],
#     [0.67, 0.33, 0.17, 1.33, 166.67],
#     [3.33, -0.83, 2.08, 6.67]
# ]
# cj = [5, 5, 0, 10]
# cb = [0, 12.5]
# print()
# print("Итеряция 2")
# print_matrix(*simplex_method(matrix, cj, cb))

# matrix = [
#     [0.71, -0.71, 0.28, -0.85, -740.74],
#     [-0.27, 1.27, -0.21, 1.14, 1151.86],
#     [-1.4, 3.9, 0.2, 5.7]
# ]
# cj = [5, 5, 0, 0]
# cb = [10, 12.5]
# print()
# print("Итеряция 3")
# print_matrix(*simplex_method(matrix, cj, cb))
# matrix = [
#     [-0.84, 0.84, -0.33, -1.18, 871.46],
#     [0.68, 0.32, 0.17, 1.34, 158.4],
#     [3.36, -0.86, 2.08, 6.71]
# ]
# cj = [5, 5, 0, 10]
# cb = [0, 12.5]
# print()
# print("Итеряция 4")
# print_matrix(*simplex_method(matrix, cj, cb))