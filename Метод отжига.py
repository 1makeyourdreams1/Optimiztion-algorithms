import numpy as np
import matplotlib.pyplot as plt
import random
import math


# Генерация случайных координат городов
def generate_cities(num_cities):
    route = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    random.shuffle(route)
    return (np.random.rand(num_cities, 2) * 100).astype(int), route



# Вычисление полной длины маршрута
def total_route_distance(route, distances):
    dist = 0
    for i in range(len(route) - 1):
        dist += distances[route[i]][route[i + 1]]
        print(distances[route[i]][route[i + 1]], " +", end=" ")
    dist += distances[route[0]][route[-1]]
    print(distances[route[0]][route[-1]])
    return dist


# Функция для решения задачи коммивояжера методом имитации отжига
def simulated_annealing(distances, initial_temp, cooling_rate, max_iter, current_route):
    num_cities = len(distances)
    current_distance = total_route_distance(current_route, distances)

    best_route = current_route[:]
    best_distance = current_distance
    changes = []

    temp = initial_temp

    for i in range(max_iter):
        new_route = current_route[:]
        city1, city2 = random.sample(range(num_cities), 2)
        changes.append((new_route[city1], new_route[city2]))

        new_route[city1], new_route[city2] = new_route[city2], new_route[city1]

        new_distance = total_route_distance(new_route, distances)

        # Если новое решение лучше, принимаем его
        if new_distance < current_distance:
            current_route = new_route
            current_distance = new_distance
            if new_distance < best_distance:
                best_route = new_route
                best_distance = new_distance
        else:
            if random.random() < math.exp((current_distance - new_distance) / temp):
                current_route = new_route
                current_distance = new_distance

        temp *= cooling_rate
        print(f"Итерация:{i}\nТемпература: {temp}\nТекущий путь: {new_distance}\nЛучший путь: {current_distance}\n\n\n")

    return best_route, best_distance, changes


# Визуализация маршрута
def plot_route(cities_coord, route):
    coords = list(cities_coord.values())
    x_coords = [item[0] for item in coords]
    y_coords = [item[1] for item in coords]
    plt.figure(figsize=(10, 6))
    plt.scatter(x_coords, y_coords, color='red')
    for i in cities_coord.keys():
        plt.text(cities_coord[i][0], cities_coord[i][1], f'{i}', fontsize=12, color='Black')

    ordered_x_coords = []
    ordered_y_coords = []
    for item in route:
        ordered_x_coords.append(cities_coord[item][0])
        ordered_y_coords.append(cities_coord[item][1])
    ordered_x_coords.append(ordered_x_coords[0])
    ordered_y_coords.append(ordered_y_coords[0])
    plt.plot(ordered_x_coords, ordered_y_coords, 'b-', lw=2)
    plt.title('Route Plot')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.show()


if __name__ == '__main__':
    num_cities = 10
    # cities_coord, route = generate_cities(num_cities)
    cities_coord = {
        'A': [41, 25],
        'B': [10, 31],
        'C': [79, 45],
        'D': [29, 11],
        'E': [87, 12],
        'F': [98, 98],
        'G': [69, 5],
        'H': [49, 72],
        'I': [13, 52],
        'J': [40, 10]
    }
    route = ['F', 'A', 'E', 'I', 'D', 'C', 'B', 'H', 'G', 'J']
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
    initial_temp = 100
    cooling_rate = 0.99
    max_iter = 100

    best_route, best_distance, changes = simulated_annealing(distances, initial_temp, cooling_rate, max_iter, route)
    print(f"Начальная длина графа: {total_route_distance(route, distances)}")

    print(f'Лучший маршрут: {best_route}')
    print(f'Минимальная длина маршрута: {best_distance:.2f}')


    # Отрисовка графа маршрута
    plot_route(cities_coord, route)
