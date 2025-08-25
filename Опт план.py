import TPR5 as simplex


def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    transposed_matrix = [[matrix[row][col] for row in range(rows)] for col in range(cols)]
    return transposed_matrix


def cut_matrix(matrix, basis):
    new_matrix = []
    for i in range(len(matrix)):
        temp = []
        for b in basis:
            temp.append(matrix[i][b - 1])
        new_matrix.append(temp)
    return new_matrix


def inverse_matrix(matrix):
    augmented_matrix = [
        [
            matrix[i][j] if j < len(matrix) else int(i == j - len(matrix))
            for j in range(2 * len(matrix))
        ]
        for i in range(len(matrix))
    ]
    for i in range(len(matrix)):
        pivot = augmented_matrix[i][i]
        for j in range(2 * len(matrix)):
            augmented_matrix[i][j] /= pivot
        for j in range(len(matrix)):
            if i != j:
                scalar = augmented_matrix[j][i]
                for k in range(2 * len(matrix)):
                    augmented_matrix[j][k] -= scalar * augmented_matrix[i][k]
    inverse = [
        [augmented_matrix[i][j] for j in range(len(matrix), 2 * len(matrix))]
        for i in range(len(matrix))
    ]
    return inverse


def duality_first_theorem(matrix, cj, basis, limits):
    new_matrix = cut_matrix(matrix, basis)
    inverse = inverse_matrix(new_matrix)
    y = []
    for i in range(len(inverse)):
        summ = 0
        for j in range(len(basis)):
            summ += cj[basis[j] - 1] * inverse[j][i]
        y.append(summ)
    ans = 0
    for i in range(len(y)):
        ans += y[i] * limits[i]
    return int(ans)


def duality_second_theorem(matrix, cj, basis, limits):
    coefficients = transpose_matrix(cut_matrix(matrix, basis))
    n = len(coefficients)
    augmented_matrix = [coefficients[i] + [cj[i]] for i in range(n)]

    # Решение системы уравнений
    for i in range(n):
        max_row = i
        for j in range(i + 1, n):
            if abs(augmented_matrix[j][i]) > abs(augmented_matrix[max_row][i]):
                max_row = j

        augmented_matrix[i], augmented_matrix[max_row] = augmented_matrix[max_row], augmented_matrix[i]

        pivot = augmented_matrix[i][i]
        augmented_matrix[i] = [x / pivot for x in augmented_matrix[i]]

        for j in range(i + 1, n):
            factor = augmented_matrix[j][i]
            augmented_matrix[j] = [augmented_matrix[j][k] - factor * augmented_matrix[i][k] for k in range(n + 1)]

    y = [0] * n
    for i in range(n - 1, -1, -1):
        y[i] = augmented_matrix[i][n]
        for j in range(i + 1, n):
            y[i] -= augmented_matrix[i][j] * y[j]
    ans = 0
    for i in range(len(y)):
        ans += y[i] * limits[i]
    return int(ans)


def duality_third_theorem(matrix, basis, limits, plan):
    new_matrix = cut_matrix(matrix, basis)
    opt_plan = []
    for b in basis:
        opt_plan.append(plan[b - 1])

    inverse = inverse_matrix(new_matrix)
    G = []
    y = [9 / 35, 0.24]
    for i in range(len(inverse)):
        temp_min = []
        temp_max = []
        for j in range(len(inverse[i])):
            if inverse[i][j] > 0:
                temp_min.append(opt_plan[j] / inverse[j][i])
            elif inverse[i][j] < 0:
                temp_max.append(abs(opt_plan[j] / inverse[j][i]))
        bottom_edge = min(temp_min)
        top_edge = max(temp_max)
        print(f"Диапазон изменения ресурса {len(inverse) - i}:"
              f" (", limits[-(i + 1)] - bottom_edge, ",", limits[-(i + 1)] + top_edge, ")")
        G.append([bottom_edge, top_edge])
    delta_G = 0
    for i in range(len(y)):
        print(f"delta_G_{i + 1} =", y[i] * G[len(G) - i - 1][1])
        delta_G += y[i] * G[len(G) - i - 1][1]
    return simplex.get_optimal_plan() + delta_G


matrix = [
    [3.5, 7, 4.2],
    [4, 5, 8],
]
limits = [1400, 2000]
cj = [1, 3, 3]
cb = [0, 0]
plan = [0, 80, 200, 0, 0]
basis = [2, 3]

print(f"Оптимальный план согласно симплексному методу: {simplex.get_optimal_plan()}")
print(f"Оптимальный план согласно первой теореме двойственности: {duality_first_theorem(matrix, cj, basis, limits)}")
print(f"Оптимальный план согласно второй теореме двойственности: "
      f"{duality_second_theorem(matrix, cj[1:], basis, limits)}")
print(f"Оптимальное значение целевой функции при максимальном изменении ресурсов: "
      f"{duality_third_theorem(matrix, basis, limits, plan)}")
