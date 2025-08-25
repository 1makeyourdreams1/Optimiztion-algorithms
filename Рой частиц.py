import sys

import numpy as np

from memory_profiler import profile

from pyinstrument import Profiler


def objective_function(x):
    """
    Целевая функция для оптимизации.
    """
    return np.sum(100 * (x[1:] - x[:-1] ** 2) ** 2 + (1 - x[:-1]) ** 2)


class Particle:
    """
    Класс, представляющий частицу в алгоритме PSO.
    """

    def __init__(self, dims, bounds):
        """
        Инициализация частицы.

        :param dims: Количество измерений.
        :param bounds: Границы поиска.
        """
        self.position = np.random.uniform(bounds[0], bounds[1], dims)
        self.velocity = np.random.uniform(bounds[0], bounds[1], dims)
        self.best_position = np.copy(self.position)
        self.best_value = float('inf')

    def update_velocity(self, global_best_position, w, c1, c2):
        """
        Обновление скорости частицы.

        :param global_best_position: Глобальное лучшее положение.
        :param w: Коэффициент инерции.
        :param c1: Когнитивный коэффициент.
        :param c2: Социальный коэффициент.
        """
        r1, r2 = np.random.rand(), np.random.rand()
        cognitive_component = c1 * r1 * (self.best_position - self.position)
        social_component = c2 * r2 * (global_best_position - self.position)
        self.velocity = w * self.velocity + cognitive_component + social_component

    def update_position(self, bounds):
        """
        Обновление позиции частицы.

        :param bounds: Границы поиска.
        """
        self.position += self.velocity
        self.position = np.clip(self.position, bounds[0], bounds[1])


class PSO:
    """
    Класс, представляющий алгоритм PSO.
    """

    def __init__(self, function, dims, bounds, num_particles,
                 w=0.5, c1=1.5, c2=1.5, max_iter=100):
        """
        Инициализация алгоритма PSO.

        :param function: Целевая функция для оптимизации.
        :param dims: Количество измерений.
        :param bounds: Границы поиска.
        :param num_particles: Количество частиц.
        :param w: Коэффициент инерции.
        :param c1: Когнитивный коэффициент.
        :param c2: Социальный коэффициент.
        :param max_iter: Максимальное количество итераций.
        """
        self.function = function
        self.dims = dims
        self.bounds = bounds
        self.num_particles = num_particles
        self.particles = [Particle(dims, bounds) for _ in range(num_particles)]
        self.global_best_position = np.random.uniform(bounds[0], bounds[1], dims)
        self.global_best_value = float('inf')
        self.params = {'w': w, 'c1': c1, 'c2': c2}
        self.max_iter = max_iter


    def memory_leak(self):
        memory_leak_list = []
        for _ in range(100000):
            memory_leak_list.append(np.random.rand(1000000))
        return
    @profile()
    def optimize(self):

        self.memory_leak()
        for t in range(self.max_iter):
            for particle in self.particles:
                fitness_value = self.function(particle.position)

                if fitness_value < particle.best_value:
                    particle.best_value = fitness_value
                    particle.best_position = np.copy(particle.position)

                if fitness_value < self.global_best_value:
                    self.global_best_value = fitness_value
                    self.global_best_position = np.copy(particle.position)

            # for i in range(100000):
            #     continue

            for particle in self.particles:
                particle.update_velocity(self.global_best_position, **self.params)
                particle.update_position(self.bounds)

        return self.global_best_position, self.global_best_value


if __name__ == "__main__":
    # Настройка параметров PSO
    DIMENSIONS = 2
    BOUNDS = (-1, 1)
    NUM_PARTICLES = 10
    MAX_ITER = 50

    # Создание профайлера
    profiler = Profiler()

    # Запуск профайлера
    profiler.start()

    # Выполнение кода, который нужно профилировать
    pso = PSO(objective_function, DIMENSIONS, BOUNDS, NUM_PARTICLES, max_iter=MAX_ITER)
    best_position, best_value = pso.optimize()

    # Остановка профайлера
    profiler.stop()

    # Вывод отчета
    print(profiler.output_text(unicode=True, color=True))


    best_position, best_value = pso.optimize()


    # print(f"Лучшее найденное положение: {best_position[0]:.15f} {best_position[1]:.15f}")
    # print(f"Лучшее значение функции: {best_value:.25f}")

