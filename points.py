class Point():
    def __init__(self, id, relations):
        self.id = id
        self.relations = relations

    @property
    def relations(self):
        return self._relations

    @relations.setter
    def relations(self, value):
        self._relations = value

    def __str__(self) -> str:
        return self.id

    def __eq__(self, __o: object) -> bool:
        return self.id == __o
