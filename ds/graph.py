class Node:
    def __init__(self, datum):
        self.datum = datum

class Edge:
    def __init__(self, from_node, to_node):
        self.from_node = from_node
        self.to_node = to_node

class Graph:
    def __init__(self, V, E):
        self.V = V
        self.E = E

