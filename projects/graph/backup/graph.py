"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
        else:
            raise IndexError(
                "That vertex has vanished w/o a trace, doesn't exist")


g_unit = Graph()
g_unit.add_vertex('0')
g_unit.add_vertex('1')
g_unit.add_vertex('2')
g_unit.add_vertex('3')
g_unit.add_edge('0', '1')
g_unit.add_edge('0', '3')
print("GRAPH VERTS", g_unit.vertices)
