import points
import dijkstra


def main():
    a = points.Node("a")
    b = points.Node("b")
    c = points.Node("c")
    d = points.Node("d")
    e = points.Node("e")
    f = points.Node("f")

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

    dijkstra.dijkstra(a, b, c, d, e, f)


if __name__ == '__main__':
    main()
