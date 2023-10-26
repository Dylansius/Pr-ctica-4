import networkx as nx
import matplotlib.pyplot as plt
import sys

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}
    
    def add_node(self, value):
        self.nodes.add(value)
        if value not in self.edges:
            self.edges[value] = []

    def add_edge(self, from_node, to_node, weight):
        self.edges[from_node].append((to_node, weight))
        self.edges[to_node].append((from_node, weight))

def prim(graph):
    mst = set()
    start_node = list(graph.nodes)[0]
    mst.add(start_node)
    total_cost = 0
    mst_graph = nx.Graph()

    while len(mst) < len(graph.nodes):
        min_edge = (None, None, sys.maxsize)
        for node in mst:
            for neighbor, weight in graph.edges[node]:
                if neighbor not in mst and weight < min_edge[2]:
                    min_edge = (node, neighbor, weight)
        
        if min_edge[1] is not None:
            mst.add(min_edge[1])
            total_cost += min_edge[2]
            print(f"Add edge: {min_edge[0]} - {min_edge[1]} (Cost: {min_edge[2]})")
            mst_graph.add_edge(min_edge[0], min_edge[1], weight=min_edge[2])

    print(f"Total Minimum Spanning Tree Cost: {total_cost}")

    # Visualización gráfica del Árbol de Expansión Mínima
    pos = nx.spring_layout(mst_graph)
    labels = nx.get_edge_attributes(mst_graph, 'weight')
    nx.draw(mst_graph, pos, with_labels=True, node_size=800, node_color='lightblue', font_size=8)
    nx.draw_networkx_edge_labels(mst_graph, pos, edge_labels=labels)
    plt.title("Minimum Spanning Tree (Prim's Algorithm)")
    plt.show()

def main():
    graph = Graph()
    graph.add_node("A")
    graph.add_node("B")
    graph.add_node("C")
    graph.add_node("D")
    graph.add_node("E")
    graph.add_edge("A", "B", 2)
    graph.add_edge("A", "C", 4)
    graph.add_edge("B", "C", 1)
    graph.add_edge("B", "D", 7)
    graph.add_edge("C", "D", 3)
    graph.add_edge("C", "E", 5)
    graph.add_edge("D", "E", 6)
    
    print("Minimum Spanning Tree (Prim's Algorithm):")
    prim(graph)

if __name__ == "__main__":
    main()
