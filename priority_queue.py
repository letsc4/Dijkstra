class PriorityQueue():
    """Class to create a priority queue which is using a dictionary. Lowest priority is the first to get out
    """

    def __init__(self) -> None:
        self._priority_queue = {}

    def __sort(self):
        """sorting queue so that lowest priority is first to get out
        """
        self._priority_queue = {key: value for key, value in sorted(
            self._priority_queue.items(), key=lambda item: item[1], reverse=True)}

    @property
    def queue(self):
        """Returns queue as a dictionary

        Returns:
            dict: queue; {object: priority}
        """
        return self._priority_queue

    def see_priority_of_object(self, object):
        """Returns the priority of a given object that already exists in the queue

        Parameters:
            object (any): object to get priority of

        Returns:
            int: priority
        """
        if object not in self._priority_queue:
            return 0
        else:
            return self._priority_queue[object]

    def put(self, object, priority: int):
        """puts new object in queue

        Parameters:
            object (any): object to put in queue
            priority (int): priority to assign to the object
        """
        self._priority_queue.update({object: priority})
        self.__sort()

    def get(self):
        """Removes item with lowest priority and returns it

        Returns:
            tuple: tuple of key and value (object, priority)
        """
        return self._priority_queue.popitem()

    def empty(self):
        """Check if queue is empty

        Returns:
            bool: Returns True if queue is empty
        """
        if self._priority_queue == {}:
            return True
        else:
            return False
