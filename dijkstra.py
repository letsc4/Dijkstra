class LowestDistanceNode():
    def __init__(self, start_node, nodes):
        self.__start_node = start_node
        self.__nodes = nodes
        self._visited_nodes = []
        self.visited_nodes = start_node
        self._node_distances = {}
        self.node_distances = nodes

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
    def node_distances(self, nodes):
        if isinstance(nodes, tuple):  # if node is tuple of nodes; for initalization
            for i in nodes:
                self._node_distances.update(
                    {i.id: None})  # CHANGE NONE TO WORK
            for o in self.__start_node.relations:
                self._node_distances.update(
                    {o: self.__start_node.relations[o]})
        else:  # if node is point object
            add_onto = self.__add_onto(nodes)

            # update values of visited notes with logic(dont update key when value higher)
            for neighbour in nodes.relations:

                if neighbour == self.__start_node.id:
                    continue
                elif self._node_distances[neighbour] == None:
                    self._node_distances.update(
                        {neighbour: nodes.relations[neighbour] + add_onto})
                elif nodes.relations[neighbour] + add_onto < self._node_distances[neighbour]:
                    self._node_distances.update(
                        {neighbour: nodes.relations[neighbour] + add_onto})

            self._visited_nodes.append(nodes)

    def __add_onto(self, node):
        return self._node_distances[node.id]

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

    nodes_object = LowestDistanceNode(start, other)
    while len(nodes_object.visited_nodes) != nodes_object.count_of_objects:
        for g in other:
            if g.id == nodes_object.lowest_distance:
                nodes_object.node_distances = g

    print(nodes_object.node_distances)
