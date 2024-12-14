from collections import deque, defaultdict

class EdmondsKarp:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.graph = defaultdict(list)
        self.capacity = defaultdict(lambda: defaultdict(int))

    def add_edge(self, u, v, capacity):
        """
        Добавляет ребро в граф с указанной пропускной способностью.
        """
        self.graph[u].append(v)
        self.graph[v].append(u)  # Добавляем обратное ребро
        self.capacity[u][v] += capacity  # Прямое ребро
        self.capacity[v][u] += 0         # Обратное ребро

    def bfs(self, source, sink, parent):
        """
        BFS для поиска увеличивающего пути.
        Возвращает True, если путь найден, иначе False.
        """
        visited = [False] * self.num_vertices
        queue = deque([source])
        visited[source] = True

        while queue:
            u = queue.popleft()
            for v in self.graph[u]:
                if not visited[v] and self.capacity[u][v] > 0:  # Есть свободная пропускная способность
                    parent[v] = u
                    if v == sink:
                        return True  # Достигли стока
                    queue.append(v)
                    visited[v] = True
        return False

    def edmonds_karp(self, source, sink):
        """
        Основная функция для вычисления максимального потока.
        """
        parent = [-1] * self.num_vertices
        max_flow = 0

        while self.bfs(source, sink, parent):
            # Находим минимальную пропускную способность на пути
            path_flow = float('Inf')
            v = sink
            while v != source:
                u = parent[v]
                path_flow = min(path_flow, self.capacity[u][v])
                v = u

            # Обновляем потоки и остаточную сеть
            v = sink
            while v != source:
                u = parent[v]
                self.capacity[u][v] -= path_flow
                self.capacity[v][u] += path_flow
                v = u

            # Увеличиваем общий поток
            max_flow += path_flow

        return max_flow


##пример реализации
if __name__ == "__main__":
    num_vertices = 6  # Пример графа с 6 вершинами
    graph = EdmondsKarp(num_vertices)

    # Добавление рёбер с их пропускной способностью
    graph.add_edge(0, 1, 16)
    graph.add_edge(0, 2, 13)
    graph.add_edge(1, 2, 10)
    graph.add_edge(1, 3, 12)
    graph.add_edge(2, 4, 14)
    graph.add_edge(3, 2, 9)
    graph.add_edge(3, 5, 20)
    graph.add_edge(4, 3, 7)
    graph.add_edge(4, 5, 4)

    source, sink = 0, 5
    max_flow = graph.edmonds_karp(source, sink)
    print(f"Максимальный поток: {max_flow}")
