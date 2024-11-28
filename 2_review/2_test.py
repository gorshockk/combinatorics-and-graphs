import time
import heapq
from random import randint

class BucketDijkstra:
    def __init__(self, graph, num_vertices):
        self.graph = graph
        self.num_vertices = num_vertices

    def shortest_path(self, start):
        dist = [float('inf')] * self.num_vertices
        dist[start] = 0
        buckets = [[] for _ in range(self.num_vertices + 1)]
        buckets[0].append(start)

        for current_bucket in range(self.num_vertices):
            while buckets[current_bucket]:
                u = buckets[current_bucket].pop()
                for v, weight in self.graph[u]:
                    new_dist = dist[u] + weight
                    if new_dist < dist[v]:
                        if dist[v] != float('inf'):
                            buckets[dist[v]].remove(v)
                        dist[v] = new_dist
                        buckets[new_dist].append(v)

        return dist


# Генерация графов для тестирования
def generate_graph(num_vertices, num_edges, max_weight=10):
    graph = [[] for _ in range(num_vertices)]
    for _ in range(num_edges):
        u, v = randint(0, num_vertices - 1), randint(0, num_vertices - 1)
        weight = randint(1, max_weight)
        graph[u].append((v, weight))
        graph[v].append((u, weight))  # Для неориентированного графа
    return graph


# Тестирование на малых графах
def test_small_graphs():
    graph = [
        [(1, 4), (2, 1)],
        [(0, 4), (3, 1)],
        [(0, 1), (3, 2)],
        [(1, 1), (2, 2)]
    ]
    dijkstra = BucketDijkstra(graph, len(graph))
    print("Shortest paths from vertex 0:", dijkstra.shortest_path(0))


# Тестирование производительности на больших графах
def test_large_graphs():
    num_vertices, num_edges = 1000, 10000
    graph = generate_graph(num_vertices, num_edges)
    dijkstra = BucketDijkstra(graph, num_vertices)

    start_time = time.time()
    dist = dijkstra.shortest_path(0)
    end_time = time.time()
    print(f"Time taken for {num_vertices} vertices and {num_edges} edges: {end_time - start_time:.2f} seconds")


# Сравнение с классической реализацией
def compare_with_classic_dijkstra():
    class ClassicDijkstra:
        def __init__(self, graph, num_vertices):
            self.graph = graph
            self.num_vertices = num_vertices

        def shortest_path(self, start):
            dist = [float('inf')] * self.num_vertices
            dist[start] = 0
            priority_queue = [(0, start)]
            while priority_queue:
                current_dist, u = heapq.heappop(priority_queue)
                if current_dist > dist[u]:
                    continue
                for v, weight in self.graph[u]:
                    new_dist = current_dist + weight
                    if new_dist < dist[v]:
                        dist[v] = new_dist
                        heapq.heappush(priority_queue, (new_dist, v))
            return dist

    num_vertices, num_edges = 500, 2000
    graph = generate_graph(num_vertices, num_edges)

    bucket_dijkstra = BucketDijkstra(graph, num_vertices)
    classic_dijkstra = ClassicDijkstra(graph, num_vertices)

    start_time = time.time()
    bucket_result = bucket_dijkstra.shortest_path(0)
    bucket_time = time.time() - start_time

    start_time = time.time()
    classic_result = classic_dijkstra.shortest_path(0)
    classic_time = time.time() - start_time

    print(f"Bucket Dijkstra time: {bucket_time:.2f} seconds")
    print(f"Classic Dijkstra time: {classic_time:.2f} seconds")
    print(f"Results match: {bucket_result == classic_result}")


# Запуск всех тестов
if __name__ == "__main__":
    print("Testing small graphs...")
    test_small_graphs()

    print("\nTesting large graphs...")
    test_large_graphs()

    print("\nComparing with classic Dijkstra...")
    compare_with_classic_dijkstra()
