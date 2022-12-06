class Graph():

    def __init__(self, start_node, nodes):
        self.__start_node = start_node
        self.__nodes = nodes

        self._node_distances = {}
        for i in nodes:
            self._node_distances.update({i.id: {}})
        # for j in start_node.relations:
        #     self._node_distances[j].update({j: start_node.relations[j]})

        self._visited_nodes = []

    @property
    def visited_nodes(self):
        return self._visited_nodes

    @visited_nodes.setter
    def visited_nodes(self, node):
        self._visited_nodes.append(node)

    @property
    def node_distances(self):
        return self._node_distances

    @node_distances.setter
    def node_distances(self, current_node, neighbour):
        self._node_distances[neighbour].update(
            {neighbour: current_node.relations[neighbour]})

    @property
    def lowest_distance(self):
        lowest_key = None
        for k in self._node_distances:
            if k in self._visited_nodes or self._node_distances[k] == None:
                continue
            elif lowest_key == None:
                lowest_key = k
            elif self._node_distances[k] < self._node_distances[lowest_key]:
                lowest_key = k

        return lowest_key  # must be string

    @property
    def count_of_objects(self):
        return len(self.__nodes) + 1



def dijkstra(start, *other):

    nodes_object = Graph(start, other)
    while len(nodes_object.visited_nodes) != nodes_object.count_of_objects:
        for g in other:
            if g.id == nodes_object.lowest_distance:
                nodes_object.node_distances = g

    print(nodes_object.node_distances)
