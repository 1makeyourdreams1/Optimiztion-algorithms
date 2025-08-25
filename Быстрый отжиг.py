import numpy as np

def rosenbrock(x, y):
    return (1 - x) ** 2 + 100 * (y - x ** 2) ** 2


# Алгоритм быстрого отжига
def fast_annealing(rosen_func, initial_temp=100, max_iter=3):
    x, y = np.random.uniform(-2, 2, 2)
    best_x, best_y = x, y
    best_score = rosen_func(x, y)


    for i in range(max_iter):
        # Снижение температуры
        temp = initial_temp / (1 + i)

        candidate_x = x + temp * np.random.standard_cauchy()
        candidate_y = y + temp * np.random.standard_cauchy()

        candidate_score = rosen_func(candidate_x, candidate_y)

        if candidate_score < best_score or np.exp((best_score - candidate_score) / temp) > np.random.rand():
            x, y = candidate_x, candidate_y
            best_x, best_y = x, y
            best_score = candidate_score

        print(f"Текущая итерация: {i + 1}")
        print(f"Значение X: {x:.4f}, Y: {y:.4f}")
        print(f"Значение функции F(x, y) = {candidate_score:.4f}")
        print(f"Текущее оптимальное значение: X = {best_x:.4f}, Y = {best_y:.4f}, F(x, y) = {best_score:.4f}\n")


    return best_x, best_y, best_score


best_x, best_y, best_score = fast_annealing(rosenbrock)
print(f"Найденный минимум функции Розенброка: x = {best_x:.4f}, y = {best_y:.4f}, значение функции = {best_score:.4f}")
