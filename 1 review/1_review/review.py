class UnionFind:
    def __init__(self, n):
        """
        Инициализация структуры данных Union-Find.
        :param n: Количество элементов (от 0 до n-1).
        """
        self.parent = list(range(n))  # Каждый элемент указывает на себя
        self.rank = [0] * n           # Ранги всех деревьев равны 0

    def find(self, x):
        """
        Поиск представителя множества (корня дерева) с применением сжатия путей.
        :param x: Элемент, для которого выполняется поиск.
        :return: Корень множества, к которому принадлежит x.
        """
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Рекурсивное сжатие путей
        return self.parent[x]

    def union(self, x, y):
        """
        Объединение двух множеств с применением объединения по рангу.
        :param x: Первый элемент.
        :param y: Второй элемент.
        """
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            # Объединяем по рангу
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

    def connected(self, x, y):
        """
        Проверяет, принадлежат ли два элемента одному множеству.
        :param x: Первый элемент.
        :param y: Второй элемент.
        :return: True, если элементы в одном множестве, иначе False.
        """
        return self.find(x) == self.find(y)

# Пример использования
if __name__ == "__main__":
    n = 10  # Количество элементов
    uf = UnionFind(n)

    # Объединяем элементы
    uf.union(1, 2)
    uf.union(3, 4)
    uf.union(2, 3)

    # Проверяем принадлежность к одному множеству
    print(uf.connected(1, 4))  # True (1, 2, 3, 4 в одном множестве)
    print(uf.connected(1, 5))  # False (5 не принадлежит этому множеству)

    # Проверяем корни элементов
    print(uf.find(1))  # Корень множества
    print(uf.find(4))  # Корень совпадает с find(1) после сжатия путей
