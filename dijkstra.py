class Graph():

    def __init__(self, start_node, nodes):
        self.__nodes = nodes

        self.node_distances = {start_node: {}}
        for i in nodes:
            self.node_distances.update({i: {}})

        self.priority_queue_nodes = {}
        self._visited_nodes = []

    @property
    def visited_nodes(self):
        return self._visited_nodes

    @visited_nodes.setter
    def visited_nodes(self, node):
        self._visited_nodes.append(node)
        self.update_priority_queue_nodes()

    def update_priority_queue_nodes(self):
        # lowest value first to get out
        if self.priority_queue_nodes:
            self.priority_queue_nodes.popitem()
        for node_id in self.node_distances:
            if node_id in self._visited_nodes:
                continue
            sum_of_values = self.add_onto(node_id)
            if sum_of_values:
                self.priority_queue_nodes.update({node_id: sum_of_values})
        # sorting by value
        self.priority_queue_nodes = {key: value for key, value in sorted(
            self.priority_queue_nodes.items(), key=lambda item: item[1], reverse=True)}

    def add_onto(self, node_id):
        """Returns sum of values of a node in node_distances

        Args:
            node_id (<class 'points.Node'>): _description_

        Returns:
            int: _description_
        """
        return sum(self.node_distances[node_id].values())

    @property
    def count_of_objects(self):
        return len(self.__nodes) + 1


def dijkstra(start, *nodes):

    nodes_object = Graph(start, nodes)
    for j in start.relations:
        nodes_object.node_distances[j].update(
            {start: start.relations[j]})
    nodes_object.visited_nodes = start

    while len(nodes_object.visited_nodes) != nodes_object.count_of_objects:
        for node in nodes:
            # choosing node that has highest priority(lowest distance) and that is also not already visited
            if nodes_object.priority_queue_nodes and node == list(nodes_object.priority_queue_nodes)[-1]:
                for neighbour in node.relations:
                    add_on = nodes_object.add_onto(neighbour)
                    if neighbour == start:
                        continue
                    elif nodes_object.node_distances[neighbour] == {}:
                        nodes_object.node_distances[neighbour].update(
                            nodes_object.node_distances[node])
                        nodes_object.node_distances[neighbour].update(
                            {node: node.relations[neighbour]})
                    # if total distance to current neighbour of current node is lower than distance to current neighbour of previous node
                    elif node.relations[neighbour] + nodes_object.add_onto(node) < add_on:
                        nodes_object.node_distances[neighbour].clear()
                        nodes_object.node_distances[neighbour].update(
                            nodes_object.node_distances[node])
                        nodes_object.node_distances[neighbour].update(
                            {node: node.relations[neighbour]})
                nodes_object.visited_nodes = node

    print(nodes_object.node_distances)
