import numpy as np


def objective_function(x):
    x1, x2 = x
    return 7 * x1 ** 2 + 2 * x1 * x2 + 5 * x2 ** 2 + x1 - 10 * x2


def hooke_jeeves(x0, step_size=1.0, alpha=0.5, epsilon=1e-6, max_iter=1000):
    x_best = np.array(x0, dtype=float)
    x_new = np.array(x0, dtype=float)
    iteration = 0

    while step_size > epsilon and iteration < max_iter:
        iteration += 1

        # Поисковое движение
        for i in range(len(x_best)):
            for delta in [step_size, -step_size]:
                x_temp = x_best.copy()
                x_temp[i] += delta
                if objective_function(x_temp) < objective_function(x_best):
                    x_best = x_temp

        # Шаг сопряжённого направления
        if not np.array_equal(x_best, x_new):
            x_pattern = x_best + (x_best - x_new)
            if objective_function(x_pattern) < objective_function(x_best):
                x_new = x_best
                x_best = x_pattern
            else:
                x_new = x_best
        else:
            step_size *= alpha  # Уменьшение шага

    return x_best, objective_function(x_best), iteration


# Начальная точка
x0 = [0, 0]

# Запуск оптимизации
solution, min_value, iterations = hooke_jeeves(x0)

print(f"Найденный минимум: x = {solution}, f(x) = {min_value}, итераций: {iterations}")
