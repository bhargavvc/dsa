Let’s explore the **graph algorithms** in detail. For each algorithm, I’ll provide:

1. **Description**: What the algorithm does.
2. **Time and Space Complexity**: Best/worst-case considerations.
3. **Optimized Python code**: Designed for scalability with large inputs.

---

## **1. Dijkstra's Algorithm**
- **Description**: Finds the shortest path from a source node to all other nodes in a graph with non-negative edge weights.
- **Best Time Complexity**: \( O(E + V \log V) \) (using a priority queue).
- **Space Complexity**: \( O(V + E) \)

### Code:
```python
import heapq

def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    pq = [(0, start)]  # (distance, node)

    while pq:
        current_distance, current_node = heapq.heappop(pq)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return distances

# Usage
graph = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5)],
    3: []
}
print(dijkstra(graph, 0))  # Shortest distances from node 0
```

---

## **2. Minimum Spanning Tree (MST)**
- **Description**: Finds the subset of edges that connect all nodes with minimum total edge weight.
- **Time Complexity**: \( O(E \log V) \) (Prim's Algorithm with a priority queue).
- **Space Complexity**: \( O(V + E) \)

### Code (Prim’s Algorithm):
```python
import heapq

def prim_mst(graph, V):
    visited = [False] * V
    pq = [(0, 0)]  # (weight, node)
    mst_weight = 0

    while pq:
        weight, node = heapq.heappop(pq)
        if visited[node]:
            continue
        visited[node] = True
        mst_weight += weight
        for neighbor, w in graph[node]:
            if not visited[neighbor]:
                heapq.heappush(pq, (w, neighbor))
    return mst_weight

# Usage
graph = {
    0: [(1, 10), (2, 6), (3, 5)],
    1: [(0, 10), (3, 15)],
    2: [(0, 6), (3, 4)],
    3: [(0, 5), (1, 15), (2, 4)]
}
print(prim_mst(graph, 4))  # Output: MST weight
```

---

## **3. Topological Sort**
- **Description**: Linear ordering of vertices in a Directed Acyclic Graph (DAG).
- **Time Complexity**: \( O(V + E) \)
- **Space Complexity**: \( O(V + E) \)

### Code:
```python
from collections import defaultdict, deque

def topological_sort(graph, V):
    in_degree = [0] * V
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    queue = deque([node for node in range(V) if in_degree[node] == 0])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return result

# Usage
graph = {
    0: [1, 2],
    1: [2],
    2: []
}
print(topological_sort(graph, 3))  # Output: [0, 1, 2]
```

---

## **4. Strongly Connected Components (SCCs)**
- **Description**: Finds maximal subsets of nodes such that every node in a subset is reachable from every other node in the subset.
- **Time Complexity**: \( O(V + E) \)
- **Space Complexity**: \( O(V + E) \)

### Code (Kosaraju's Algorithm):
```python
from collections import defaultdict

def kosaraju_scc(graph, V):
    def dfs(v, visited, stack):
        visited[v] = True
        for neighbor in graph[v]:
            if not visited[neighbor]:
                dfs(neighbor, visited, stack)
        stack.append(v)

    def reverse_graph(graph):
        reversed_graph = defaultdict(list)
        for node in graph:
            for neighbor in graph[node]:
                reversed_graph[neighbor].append(node)
        return reversed_graph

    stack = []
    visited = [False] * V
    for i in range(V):
        if not visited[i]:
            dfs(i, visited, stack)

    reversed_graph = reverse_graph(graph)
    visited = [False] * V
    sccs = []

    while stack:
        node = stack.pop()
        if not visited[node]:
            component = []
            dfs(node, visited, component)
            sccs.append(component)
    return sccs

# Usage
graph = {
    0: [1],
    1: [2],
    2: [0],
    3: [4],
    4: []
}
print(kosaraju_scc(graph, 5))  # Output: [[0, 2, 1], [3], [4]]
```

---

## **5. Maximum Flow (Ford-Fulkerson Algorithm)**
- **Description**: Finds the maximum flow in a flow network.
- **Time Complexity**: \( O(E \cdot f) \) (where \( f \) is the maximum flow).
- **Space Complexity**: \( O(V + E) \)

### Code:
```python
from collections import defaultdict, deque

def bfs_capacity(graph, source, sink, parent):
    visited = set()
    queue = deque([source])
    visited.add(source)

    while queue:
        node = queue.popleft()
        for neighbor, capacity in graph[node].items():
            if neighbor not in visited and capacity > 0:
                parent[neighbor] = node
                if neighbor == sink:
                    return True
                queue.append(neighbor)
                visited.add(neighbor)
    return False

def ford_fulkerson(graph, source, sink):
    residual_graph = defaultdict(lambda: defaultdict(int))
    for u in graph:
        for v, capacity in graph[u].items():
            residual_graph[u][v] = capacity

    parent = {}
    max_flow = 0

    while bfs_capacity(residual_graph, source, sink, parent):
        path_flow = float('inf')
        s = sink
        while s != source:
            path_flow = min(path_flow, residual_graph[parent[s]][s])
            s = parent[s]

        max_flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            residual_graph[u][v] -= path_flow
            residual_graph[v][u] += path_flow
            v = parent[v]

    return max_flow

# Usage
graph = {
    0: {1: 10, 2: 10},
    1: {2: 2, 3: 4},
    2: {3: 8},
    3: {}
}
print(ford_fulkerson(graph, 0, 3))  # Output: Maximum flow
```

---

## **6. Floyd-Warshall Algorithm**
- **Description**: Finds shortest paths between all pairs of nodes.
- **Time Complexity**: \( O(V^3) \)
- **Space Complexity**: \( O(V^2) \)

### Code:
```python
def floyd_warshall(graph, V):
    dist = [[float('inf')] * V for _ in range(V)]
    for i in range(V):
        dist[i][i] = 0
    for u in graph:
        for v, w in graph[u]:
            dist[u][v] = w

    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

# Usage
graph = {
    0: [(1, 3), (2, 8)],
    1: [(2, 1)],
    2: [(0, 4)]
}
print(floyd_warshall(graph, 3))  # Output: Shortest path matrix
```

---

Would you like more details or additional algorithms? Let me know!