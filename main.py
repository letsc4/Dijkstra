from nodes import Node
from dijkstra import dijkstra


def main():
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")

    a_relations = {b: 7, c: 9, f: 14}
    b_relations = {a: 7, c: 10, d: 15}
    c_relations = {a: 9, b: 10, f: 2, d: 11}
    d_relations = {a: 15, c: 11, e: 6}
    e_relations = {d: 6, f: 9}
    f_relations = {a: 14, c: 2, e: 9}

    a.relations = a_relations
    b.relations = b_relations
    c.relations = c_relations
    d.relations = d_relations
    e.relations = e_relations
    f.relations = f_relations

    print(a, a.relations)
    print(b, b.relations)
    print(c, c.relations)
    print(d, d.relations)
    print(e, e.relations)
    print(f, f.relations)

    result = dijkstra(a, b, c, d, e, f)
    print(result)


if __name__ == '__main__':
    main()
