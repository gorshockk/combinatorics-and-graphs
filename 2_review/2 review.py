import networkx as nx


def dijkstra_with_buckets(graph, start):
    # Инициализация
    dist = {node: float('inf') for node in graph.nodes()}
    dist[start] = 0
    buckets = [[] for _ in range(len(graph.nodes()))]  # Черпаки для хранения вершин

    buckets[0].append(start)

    while any(buckets):  # Пока есть элементы в черпаках
        # Извлечение вершины с минимальным расстоянием
        for i in range(len(buckets)):
            if buckets[i]:
                u = buckets[i].pop(0)
                break

        # Обновление расстояний до соседей
        for v, weight in graph[u].items():
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                buckets[dist[v]].append(v)  # Помещаем в соответствующий черпак

    return dist
