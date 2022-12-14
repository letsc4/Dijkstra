from priority_queue import PriorityQueue


class Graph():
    """class to put the nodes into
    """

    def __init__(self, start_node, nodes):
        # setting all nodes to no distance(empty dictionary), representing infinity
        self.node_distances = {start_node: {}}
        for i in nodes:
            self.node_distances.update({i: {}})

    def sum_of(self, node):
        """Returns sum of values of a node in node_distances

        Parameters:
            node_id (<class 'nodes.Node'>): Node to get the total sum of the distances of

        Returns:
            int: total sum of the distance
        """
        return sum(self.node_distances[node].values())


def update_graph(graph, current_node, current_neighbour):
    """updating values of graph with current node and neighbour

    Parameters:
        graph (<class 'dijkstra.Graph'>): graph
        current_node (<class 'nodes.Node'>): current node
        current_neighbour (<class 'nodes.Node'>): current neighbour
    """
    # clear current values for neighbour
    graph.node_distances[current_neighbour].clear()

    # update with the values of the current node; the way to the current node
    graph.node_distances[current_neighbour].update(
        graph.node_distances[current_node])

    # update with the values to the current neighbour; the way to the current neighbour
    graph.node_distances[current_neighbour].update(
        {current_node: current_node.relations[current_neighbour]})


def dijkstra(start, *nodes):
    """Dijkstra algorithm using priority queue for Node class

    Parameters:
        start (<class 'nodes.Node'>): starting node
        nodes (<class 'nodes.Node'>): all other nodes(as many as you want)
    """
    # initializing priority queue
    to_be_visited = PriorityQueue()

    # initializing graph
    graph = Graph(start, nodes)

    # initializing distances from start
    for j in start.relations:
        update_graph(graph, start, j)
        to_be_visited.put(j, graph.sum_of(j))

    # exit loop when priority queue is empty, all nodes are visited
    while not to_be_visited.empty():

        # choosing node that has highest priority(lowest distance) and that is also not already visited
        current_node = to_be_visited.get()[0]
        # looping over neighbours of current(lowest distance) node
        for current_neighbour in current_node.relations:
            # if neighbour is starting point
            if current_neighbour == start:
                continue

            # if neighbour has no distances yet or if total distance to current neighbour of current node is lower than distance to current neighbour of previous node
            elif graph.node_distances[current_neighbour] == {} or current_node.relations[current_neighbour] + graph.sum_of(current_node) < graph.sum_of(current_neighbour):
                update_graph(graph, current_node, current_neighbour)
                # update priority queue with new neighbour
                to_be_visited.put(
                    current_neighbour, graph.sum_of(current_neighbour))

    return graph.node_distances
