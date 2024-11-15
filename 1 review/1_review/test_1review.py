from review import UnionFind
import time
import random
import matplotlib.pyplot as plt
# Тестирование алгоритма Union-Find
def test_union_find():
    sizes = [100, 1000, 10_000, 100_000, 1_000_000]  # Разные размеры для тестов
    times = []

    for size in sizes:
        uf = UnionFind(size)

        # Генерация случайных операций union и find
        operations = [(random.randint(0, size - 1), random.randint(0, size - 1)) for _ in range(size)]

        start_time = time.time()

        # Выполнение операций union
        for x, y in operations:
            uf.union(x, y)

        # Выполнение операций find
        for x, y in operations:
            uf.find(x)

        end_time = time.time()
        times.append(end_time - start_time)

    return sizes, times

# Сравнение с базовой реализацией Union-Find (без оптимизаций)
def baseline_union_find_test():
    class BaselineUnionFind:
        def __init__(self, n):
            self.parent = list(range(n))

        def find(self, x):
            while self.parent[x] != x:
                x = self.parent[x]
            return x

        def union(self, x, y):
            rootX = self.find(x)
            rootY = self.find(y)
            if rootX != rootY:
                self.parent[rootY] = rootX

    sizes = [100, 1000, 10_000, 100_000, 1_000_000]
    times = []

    for size in sizes:
        uf = BaselineUnionFind(size)
        operations = [(random.randint(0, size - 1), random.randint(0, size - 1)) for _ in range(size)]

        start_time = time.time()

        for x, y in operations:
            uf.union(x, y)

        for x, y in operations:
            uf.find(x)

        end_time = time.time()
        times.append(end_time - start_time)

    return sizes, times

# Построение графика
def plot_results():
    sizes, optimized_times = test_union_find()
    _, baseline_times = baseline_union_find_test()

    plt.figure(figsize=(10, 6))
    plt.plot(sizes, optimized_times, label="Union-Find с оптимизациями", marker='o')
    plt.plot(sizes, baseline_times, label="Union-Find без оптимизаций", marker='x')
    plt.xlabel("Размер входных данных")
    plt.ylabel("Время выполнения (секунды)")
    plt.title("Сравнение Union-Find с и без оптимизаций")
    plt.legend()
    plt.grid()
    plt.show()

# Запуск тестов
plot_results()