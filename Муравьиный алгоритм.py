import numpy as np
import random

np.random.seed(42)









num_ants = 30
num_iterations = 50
alpha = 1.5
beta = 1.25
rho = 1
Q = 1

distances = {
    'A': {'A': 0, 'B': 32, 'C': 43, 'D': 18, 'E': 48, 'F': 93, 'G': 34, 'H': 48, 'I': 39, 'J': 15},
    'B': {'A': 32, 'B': 0, 'C': 70, 'D': 28, 'E': 79, 'F': 111, 'G': 64, 'H': 57, 'I': 21, 'J': 37},
    'C': {'A': 43, 'B': 70, 'C': 0, 'D': 60, 'E': 34, 'F': 56, 'G': 41, 'H': 40, 'I': 66, 'J': 52},
    'D': {'A': 18, 'B': 28, 'C': 60, 'D': 0, 'E': 58, 'F': 111, 'G': 40, 'H': 64, 'I': 44, 'J': 11},
    'E': {'A': 48, 'B': 79, 'C': 34, 'D': 58, 'E': 0, 'F': 87, 'G': 19, 'H': 71, 'I': 84, 'J': 47},
    'F': {'A': 93, 'B': 111, 'C': 56, 'D': 111, 'E': 87, 'F': 0, 'G': 97, 'H': 55, 'I': 97, 'J': 105},
    'G': {'A': 34, 'B': 64, 'C': 41, 'D': 40, 'E': 19, 'F': 97, 'G': 0, 'H': 70, 'I': 73, 'J': 29},
    'H': {'A': 48, 'B': 57, 'C': 40, 'D': 64, 'E': 71, 'F': 55, 'G': 70, 'H': 0, 'I': 41, 'J': 63},
    'I': {'A': 39, 'B': 21, 'C': 66, 'D': 44, 'E': 84, 'F': 97, 'G': 73, 'H': 41, 'I': 0, 'J': 50},
    'J': {'A': 15, 'B': 37, 'C': 52, 'D': 11, 'E': 47, 'F': 105, 'G': 29, 'H': 63, 'I': 50, 'J': 0}
}

cities = list(distances.keys())
num_cities = len(cities)
pheromone_matrix = {city1: {city2: 0.01 for city2 in cities} for city1 in cities}
eta = {city1: {city2: 1.0 / distances[city1][city2] if city1 != city2 else 0 for city2 in cities} for city1 in cities}

def calculate_probabilities(current_city, visited):
    unvisited = [city for city in cities if city not in visited]
    tau_eta = np.array([
        (pheromone_matrix[current_city][city] ** alpha) * (eta[current_city][city] ** beta)
        for city in unvisited
    ])
    probabilities = tau_eta / tau_eta.sum()
    return unvisited, probabilities

def ant_colony_optimization():
    global pheromone_matrix
    best_path = None
    best_length = float('inf')

    for it in range(num_iterations):
        all_paths = []
        all_lengths = []

        print(f"\nИтерация {it + 1}")

        for ant in range(num_ants):
            # visited = [random.choice(cities)]  # случайный старт
            visited = [cities[0]]
            path_length = 0

            while len(visited) < num_cities:
                current_city = visited[-1]
                unvisited, probabilities = calculate_probabilities(current_city, visited)
                next_city = np.random.choice(unvisited, p=probabilities)
                visited.append(next_city)
                path_length += distances[current_city][next_city]

            path_length += distances[visited[-1]][visited[0]]
            all_paths.append(visited)
            all_lengths.append(path_length)

            print(f"  Муравей {ant + 1}: Маршрут: {[str(i) for i in visited]}, Длина: {path_length}")

            if path_length < best_length:
                best_length = path_length
                best_path = visited

        unique_paths = []
        for path in all_paths:
            if path not in unique_paths:
                unique_paths.append(path)
        # if len(unique_paths) == 1:
        #     print("Все муравьи выбрали один маршрут")
        #     return best_path, best_length
        # Испарение феромонов
        for city1 in cities:
            for city2 in cities:
                pheromone_matrix[city1][city2] *= (1 - rho)

        # Обновление феромонов для всех муравьев
        for path, length in zip(all_paths, all_lengths):
            for i in range(len(path) - 1):
                pheromone_matrix[path[i]][path[i + 1]] += Q / length
            pheromone_matrix[path[-1]][path[0]] += Q / length

        # Глобальное обновление феромонов для лучшего пути
        for i in range(len(best_path) - 1):
            pheromone_matrix[best_path[i]][best_path[i + 1]] += (Q / best_length) * 10
        pheromone_matrix[best_path[-1]][best_path[0]] += (Q / best_length) * 10

        print(f"Лучший маршрут после итерации {it + 1}: {[str(i) for i in best_path]}, Длина: {best_length}")

    return best_path, best_length

best_path, best_length = ant_colony_optimization()
print(f"\nНаилучший найденный маршрут: {[str(i) for i in best_path]}")
print(f"Длина наилучшего маршрута: {best_length}")
