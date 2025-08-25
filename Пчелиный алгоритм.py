import numpy as np

# np.random.seed(100)


def rosenbrock(coords):
    x, y = coords
    return 100 * (y - x ** 2) ** 2 + (1 - x) ** 2


class BeeAlgorithm:
    def __init__(self, S, delta=1, euclidean_distance=1, tau=500):
        self.S = S  # Количество пчел
        self.delta = delta  # Радиус области объединения
        self.euclidean_distance = euclidean_distance  # Размер шага при поиске новой точки
        self.tau = tau

    def form_subregions(self, bees):
        subregions = []
        remaining_bees = bees.copy()

        print("\nФормирование подобластей...")
        while len(remaining_bees) > 0:
            base_bee = remaining_bees[0]
            subregion = [base_bee]
            remaining_bees = remaining_bees[1:]
            print(f"\nБазовая пчела: ({base_bee[0]:.2f}, {base_bee[1]:.2f})")

            i = 0
            while i < len(remaining_bees):
                distance = np.linalg.norm(base_bee - remaining_bees[i])
                print(
                    f"    Расстояние до пчелы ({remaining_bees[i][0]:.2f}, {remaining_bees[i][1]:.2f}) = {distance:.2f}")
                if distance < self.euclidean_distance:
                    print(f"    Пчела ({remaining_bees[i][0]:.2f}, {remaining_bees[i][1]:.2f}) добавлена в подобласть.")
                    subregion.append(remaining_bees[i])
                    remaining_bees = np.delete(remaining_bees, i, axis=0)
                else:
                    i += 1

            subregions.append(subregion)
            print(f"Сформирована подобласть с {len(subregion)} пчелами.")

        return subregions

    def local_search(self, subregion):
        best_bee = subregion[0]
        best_value = rosenbrock((best_bee[0], best_bee[1]))
        print(f"  Исходная лучшая точка в подобласти: x = {best_bee[0]:.4f}, y = {best_bee[1]:.4f}, f(x, y) = {best_value:.4f}")

        for center_bee in subregion:
            print(f"\n  Поиск из точки ({center_bee[0]:.4f}, {center_bee[1]:.4f})")
            candidate_bees = []
            for _ in range(self.S - 1):
                random_offset = np.random.uniform(-self.delta, self.delta, 2)
                new_bee = center_bee + random_offset
                new_bee_value = rosenbrock((new_bee[0], new_bee[1]))
                candidate_bees.append((new_bee, new_bee_value))
                print(f"Случайная точка: ({new_bee[0]:.4f}, {new_bee[1]:.4f}) = {new_bee_value:.4f}")

            candidate_bees.sort(key=lambda x: x[1])
            best_candidate_bee, best_candidate_value = candidate_bees[0]

            repeat_count = 0
            while best_candidate_value < best_value and repeat_count < self.tau:
                repeat_count += 1
                best_value = best_candidate_value
                best_bee = best_candidate_bee
                print(f"Обновление лучшей точки: ({best_bee[0]:.4f}, {best_bee[1]:.4f}) = {best_value:.4f}")

                candidate_bees = []
                for _ in range(self.S - 1):
                    random_offset = np.random.uniform(-self.delta, self.delta, 2)
                    new_bee = best_bee + random_offset
                    new_bee_value = rosenbrock((new_bee[0], new_bee[1]))
                    candidate_bees.append((new_bee, new_bee_value))
                    print(f"Случайная точка: ({new_bee[0]:.4f}, {new_bee[1]:.4f}) = {new_bee_value:.4f}")

                candidate_bees.sort(key=lambda x: x[1])
                best_candidate_bee, best_candidate_value = candidate_bees[0]

        print(f"\n  Итоговая лучшая точка в этой подобласти: ({best_bee[0]:.4f}, {best_bee[1]:.4f}) = {best_value:.4f}")
        return best_bee, best_value

    def run(self):
        # Инициализация пчел
        bees = np.random.uniform(-5, 5, (self.S, 2))
        fitness = np.apply_along_axis(rosenbrock, 1, bees)

        print("Начальные значения:")
        for i in range(len(bees)):
            print(f"{i + 1}: ({bees[i][0]:.4f}, {bees[i][1]:.4f}) = {fitness[i]:.4f}")

        sorted_indices = np.argsort(fitness)
        bees = bees[sorted_indices]
        fitness = fitness[sorted_indices]

        print(
            f"\nГлобальная лучшая пчела: ({bees[0][0]:.4f}, {bees[0][1]:.4f}) = {fitness[0]:.4f}")

        best_bee, best_value = bees[0], fitness[0]

        # Формируем подобласти
        subregions = self.form_subregions(bees)

        # Для каждой подобласти проводим локальный поиск
        for idx, subregion in enumerate(subregions):
            print(f"\nОбработка подобласти {idx + 1}...")
            local_best_bee, local_best_value = self.local_search(subregion)
            if local_best_value < best_value:
                best_bee, best_value = local_best_bee, local_best_value

        print(f"\nЛучшее глобальное решение: x = {best_bee[0]:.4f}, y = {best_bee[1]:.4f}, f(x, y) = {best_value:.4f}")
        return best_bee, best_value


n_bees = 100

bee_algorithm = BeeAlgorithm(S=n_bees)
best_bee, best_value = bee_algorithm.run()

