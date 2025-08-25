import sympy.core.symbol
from sympy import symbols, Eq, solve

def northwest_corner(matrix, mas_A, mas_B):
    total_cost = 0
    pointer = 0
    enable_matrix = [[False] * len(matrix[i]) for i in range(len(matrix))]
    print("total_cost = ", end="")
    for i in range(len(mas_A)):
        while mas_A[i] != 0:
            if mas_A[i] >= mas_B[pointer]:
                print(mas_B[pointer], '*', matrix[i][pointer], end=" + ")
                total_cost += mas_B[pointer] * matrix[i][pointer]
                mas_A[i] -= mas_B[pointer]
                enable_matrix[i][pointer] = True
                pointer += 1
            else:
                print(mas_A[i], '*', matrix[i][pointer], end=" + ")
                total_cost += mas_A[i] * matrix[i][pointer]
                mas_B[pointer] -= mas_A[i]
                enable_matrix[i][pointer] = True
                mas_A[i] = 0
    print("= ", end="")
    return total_cost, enable_matrix


matrix = [
    [16, 30, 17, 10, 16],
    [20, 27, 26, 9, 23],
    [13, 4, 22, 3, 1],
    [2, 1, 5, 4, 24]
]
mas_A = [4, 6, 10, 10]
mas_B = [7, 7, 7, 7, 2]

total_cost, en = northwest_corner(matrix, mas_A, mas_B)
print(total_cost)

u1, u2, u3, u4 = symbols('u1 u2 u3 u4')
v1, v2, v3, v4, v5 = symbols('v1 v2 v3 v4 v5')


# print("Итерация 1")
#
# eq1 = Eq(u1 + v1, 16)
# eq2 = Eq(u2 + v1, 20)
# eq3 = Eq(u2 + v2, 27)
# eq4 = Eq(u3 + v2, 4)
# eq5 = Eq(u3 + v3, 22)
# eq6 = Eq(u4 + v3, 5)
# eq7 = Eq(u4 + v4, 4)
# eq8 = Eq(u4 + v5, 24)
# eq9 = Eq(u1, 0)
# print("Итерация 2")
# en = [
#     [True, False, False, False, True],
#     [True, True, False, False, False],
#     [False, True, True, False, False],
#     [False, False, True, True, False]
# ]
#
# eq1 = Eq(u1 + v1, 16)
# eq2 = Eq(u2 + v1, 20)
# eq3 = Eq(u2 + v2, 27)
# eq4 = Eq(u3 + v2, 4)
# eq5 = Eq(u3 + v3, 22)
# eq6 = Eq(u4 + v3, 5)
# eq7 = Eq(u4 + v4, 4)
# eq8 = Eq(u1 + v5, 16)
# eq9 = Eq(u1, 0)
# print("Итерация 3")
# en = [
#     [True, False, False, False, True],
#     [True, False, False, True, False],
#     [False, True, True, False, False],
#     [False, False, True, True, False]
# ]
# print("Итерация 4")
# en = [
#     [True, False, False, False, False],
#     [True, False, False, True, False],
#     [False, True, True, False, True],
#     [False, False, True, True, False]
# ]
# eq1 = Eq(u1 + v1, 16)
# eq2 = Eq(u2 + v1, 20)
# eq3 = Eq(u2 + v4, 9)
# eq4 = Eq(u3 + v2, 4)
# eq5 = Eq(u3 + v3, 22)
# eq6 = Eq(u4 + v3, 5)
# eq7 = Eq(u4 + v4, 4)
# eq8 = Eq(u3 + v5, 1)
# eq9 = Eq(u1, 0)
# print("Итерация 5")
# en = [
#     [True, False, False, False, False],
#     [True, False, False, True, False],
#     [True, True, False, False, True],
#     [False, False, True, True, False]
# ]
# eq1 = Eq(u1 + v1, 16)
# eq2 = Eq(u2 + v1, 20)
# eq3 = Eq(u2 + v4, 9)
# eq4 = Eq(u3 + v2, 4)
# eq5 = Eq(u3 + v1, 13)
# eq6 = Eq(u4 + v3, 5)
# eq7 = Eq(u4 + v4, 4)
# eq8 = Eq(u3 + v5, 1)
# eq9 = Eq(u1, 0)
# print("Итерация 6")
# en = [
#     [True, False, False, False, False],
#     [False, False, False, True, False],
#     [True, True, False, False, True],
#     [True, False, True, True, False]
# ]
# eq1 = Eq(u1 + v1, 16)
# eq2 = Eq(u4 + v1, 2)
# eq3 = Eq(u2 + v4, 9)
# eq4 = Eq(u3 + v2, 4)
# eq5 = Eq(u3 + v1, 13)
# eq6 = Eq(u4 + v3, 5)
# eq7 = Eq(u4 + v4, 4)
# eq8 = Eq(u3 + v5, 1)
# eq9 = Eq(u1, 0)
# print("Итерация 7")
# en = [
#     [True, False, False, False, False],
#     [False, False, False, True, False],
#     [False, True, False, True, True],
#     [True, False, True, False, False]
# ]
# eq1 = Eq(u1 + v1, 16)
# eq2 = Eq(u4 + v1, 2)
# eq3 = Eq(u2 + v4, 9)
# eq4 = Eq(u3 + v2, 4)
# eq5 = Eq(u3 + v4, 3)
# eq6 = Eq(u4 + v3, 5)
# eq7 = Eq(u2, 0)
# eq8 = Eq(u3 + v5, 1)
# eq9 = Eq(u1, 0)
print("Итерация 7")
en = [
    [False, False, True, False, False],
    [False, False, False, True, False],
    [False, True, False, True, True],
    [True, False, True, False, False]
]
eq1 = Eq(u1 + v3, 17)
eq2 = Eq(u4 + v1, 2)
eq3 = Eq(u2 + v4, 9)
eq4 = Eq(u3 + v2, 4)
eq5 = Eq(u3 + v4, 3)
eq6 = Eq(u4 + v3, 5)
eq7 = Eq(u2, 0)
eq8 = Eq(u3 + v5, 1)
eq9 = Eq(u1, 0)
solution = solve([eq1, eq2, eq3, eq4, eq5, eq6, eq7, eq8, eq9], [u1, u2, u3, u4, v1, v2, v3, v4, v5])
for key, value in solution.items():
    print(key, "=", value)
print("_____________________________")
for i in range(len(en)):
    for j in range(len(en[i])):
        if not en[i][j]:
            print(f"d{i + 1}{j + 1} =", matrix[i][j], "-",  (solution[sympy.core.symbol.Symbol(f'u{i + 1}')] +
                                                               solution[sympy.core.symbol.Symbol(f'v{j + 1}')]), "=",
                  matrix[i][j] - (solution[sympy.core.symbol.Symbol(f'u{i + 1}')] +
                                  solution[sympy.core.symbol.Symbol(f'v{j + 1}')]))
            d = matrix[i][j] - (solution[sympy.core.symbol.Symbol(f'u{i + 1}')] + solution[sympy.core.symbol.Symbol(f'v{j + 1}')])






