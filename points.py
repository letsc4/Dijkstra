class Node:
    def __init__(self, id) -> None:
        self.id = id
        self.relations = {}

    def __repr__(self) -> str:
        return self.id

    def __eq__(self, __o: object) -> bool:
        return self.id == __o

    def __hash__(self):
        return hash(self.id)
