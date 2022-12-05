import points
import dijkstra


def main():
    a_relations = {"b": 7, "c": 9, "f": 14}
    b_relations = {"a": 7, "c": 10, "d": 15}
    c_relations = {"a": 9, "b": 10, "f": 2, "d": 11}
    d_relations = {"b": 15, "c": 11, "e": 6}
    e_relations = {"d": 6, "f": 9}
    f_relations = {"a": 14, "c": 2, "e": 9}

    a = points.Point("a", a_relations)
    b = points.Point("b", b_relations)
    c = points.Point("c", c_relations)
    d = points.Point("d", d_relations)
    e = points.Point("e", e_relations)
    f = points.Point("f", f_relations)

    print(a, a.relations)
    print(b, b.relations)
    print(c, c.relations)
    print(d, d.relations)
    print(e, e.relations)
    print(f, f.relations)

    dijkstra.dijkstra(a, b, c, d, e, f)


if __name__ == '__main__':
    main()
