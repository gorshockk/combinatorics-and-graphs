import networkx as nx
import random
import time
from script import EdmondsKarp

def test_small_graph():
    """
    Тест на малом графе с известным решением.
    """
    graph = EdmondsKarp(6)
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
    print(f"Максимальный поток (малый граф): {max_flow}")
    assert max_flow == 23, "Ожидаемое значение: 23"

def test_with_networkx():
    """
    Сравнение с реализацией из networkx.
    """
    num_vertices = 6
    edges = [
        (0, 1, 16),
        (0, 2, 13),
        (1, 2, 10),
        (1, 3, 12),
        (2, 4, 14),
        (3, 2, 9),
        (3, 5, 20),
        (4, 3, 7),
        (4, 5, 4)
    ]

    # Создание графа EdmondsKarp
    graph = EdmondsKarp(num_vertices)
    for u, v, capacity in edges:
        graph.add_edge(u, v, capacity)

    # Создание графа networkx
    nx_graph = nx.DiGraph()
    for u, v, capacity in edges:
        nx_graph.add_edge(u, v, capacity=capacity)

    source, sink = 0, 5
    max_flow = graph.edmonds_karp(source, sink)
    nx_flow_value = nx.maximum_flow_value(nx_graph, source, sink)

    print(f"Максимальный поток (networkx): {nx_flow_value}")
    print(f"Максимальный поток (Edmonds-Karp): {max_flow}")
    assert max_flow == nx_flow_value, "Результаты должны совпадать"

def test_large_graph():
    """
    Тест на крупном графе.
    """
    num_vertices = 1000
    num_edges = 5000
    graph = EdmondsKarp(num_vertices)

    for _ in range(num_edges):
        u = random.randint(0, num_vertices - 1)
        v = random.randint(0, num_vertices - 1)
        capacity = random.randint(1, 100)
        if u != v:
            graph.add_edge(u, v, capacity)

    source, sink = 0, num_vertices - 1

    start_time = time.time()
    max_flow = graph.edmonds_karp(source, sink)
    elapsed_time = time.time() - start_time

    print(f"Максимальный поток (крупный граф): {max_flow}")
    print(f"Время выполнения: {elapsed_time:.2f} секунд")

if __name__ == "__main__":
    test_small_graph()
    test_with_networkx()
    test_large_graph()
