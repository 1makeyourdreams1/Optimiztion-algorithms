import numpy as np

np.random.seed(8)
def rosenbrock(x, y):
    return 100.0 * (y - x**2)**2 + (1 - x)**2


class CulturalAlgorithm:
    def __init__(self, population_size, bounds, generations):
        self.population_size = population_size
        self.bounds = np.array(bounds)
        self.generations = generations

        self.population = np.random.uniform(
            low=self.bounds[0], high=self.bounds[1], size=(population_size, 2)
        )

        self.belief_space = {
            "normative": {
                "min": self.bounds[0],
                "max": self.bounds[1]
            }
        }

    def evaluate_population(self):
        return np.array([rosenbrock(ind[0], ind[1]) for ind in self.population])


    def influence_population(self):
        normative = self.belief_space["normative"]
        for i in range(self.population_size):
            self.population[i] = np.clip(
                self.population[i], normative["min"], normative["max"]
            )


    def update_belief_space(self, elites):
        self.belief_space["normative"]["min"] = (
            np.maximum(np.min(elites, axis=0), self.bounds[0])
        )
        self.belief_space["normative"]["max"] = (
            np.minimum(np.max(elites, axis=0) , self.bounds[1])
        )

    def evolve(self):

        for generation in range(self.generations):
            fitness = self.evaluate_population()
            print(f"fПоколение {generation + 1}:")
            for item in self.population:
                print(
                    f"f({np.round(item[0], 2)},{np.round(item[1], 2)})={np.round(rosenbrock(item[0], item[1]), 2)}")

            # Найти элиту
            elite_fraction = 0.2
            elite_indices = np.argsort(fitness)[:int(self.population_size * elite_fraction)]
            elites = self.population[elite_indices]
            print(f"Элиты: {np.round(elites, 2)}")

            # Вывод текущих результатов
            best_index = np.argmin(fitness)
            print(f"Лучшие значения, x = {np.round(self.population[best_index][0], 4)}, y = "
                  f"{np.round(self.population[best_index][1], 4)}, f(x, y) = "
                  f"{np.round(fitness[best_index], 4)}")

            # Обновить пространство знаний
            self.update_belief_space(elites)
            print(f"Границы после обновления: min = {np.round(self.belief_space['normative']['min'], 2)}, max = {np.round(self.belief_space['normative']['max'], 2)}")

            # Влияние пространства знаний
            self.influence_population()
            print("Популяция под влиянием пространства знаний")
            for item in self.population:
                print(f"({np.round(item[0], 2)}, {np.round(item[1], 2)})")



            # Эволюция
            new_population = []
            mutation_scale = 0.1 * (1 - generation / self.generations)
            for _ in range(self.population_size):
                parents = self.population[np.random.choice(self.population_size, 2, replace=False)]
                offspring = np.mean(parents, axis=0)  # Кроссовер
                mutation = np.random.normal(0, mutation_scale, size=2)
                offspring += mutation  # Мутация
                new_population.append(offspring)

            self.population = np.array(new_population)

            print("Новая популяция")
            for item in self.population:
                print(f"({np.round(item[0], 2)}, {np.round(item[1], 2)})")

        # Финальный результат
        fitness = self.evaluate_population()
        best_index = np.argmin(fitness)
        return self.population[best_index], fitness[best_index]


pop_size = 10
bounds = [-5, 5]
generations = 1000

ca = CulturalAlgorithm(pop_size, bounds, generations)
best_solution, best_fitness = ca.evolve()

print(f"Лучшее решение: x, y = {best_solution},  f(x, y) = {best_fitness:.7f}")
