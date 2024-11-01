class Graph:
    def __init__(self) -> None:
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, v1, v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)

    def remove_vertex(self, vertex):
        if vertex in self.adj_list:
            # Always iterate over a copy of the vertextes
            for other_vertex in list(self.adj_list[vertex]):
                self.adj_list[other_vertex].remove(vertex)
            
            # Deleting vertex after removing connections
            del self.adj_list[vertex]

            return True
        return False

    def print_items(self):
        for k, v in self.adj_list.items():
            print(f"{k} : {v}")

# Example usage
graph = Graph()
graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_edge(1, 2)
graph.add_edge(1, 3)

# Remove vertex 2
print("Before removing vertex 2:")
graph.print_items()

graph.remove_vertex(2)

print("\nAfter removing vertex 2:")
graph.print_items()


'''
remove vertext approach
first identifyning vertex exists in keys
iterating the vertext values list 
it helps to identify in which key hodling the value of vertex

because graph is interconnected so we folowed reverse appraoch
'''