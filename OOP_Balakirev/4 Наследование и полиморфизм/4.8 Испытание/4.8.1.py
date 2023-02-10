import math


class Vertex:

    def __init__(self):
        self._links = []
        self.neighbour = {}

    @property
    def links(self):
        return self._links

    @links.setter
    def links(self, value):
        self._links = value

    def init_vertex(self):
        self.neighbour = {}
        for link in self._links:
            if link.v1 != self:
                self.neighbour[link.v1] = link.dist
            if link.v2 != self:
                self.neighbour[link.v2] = link.dist


class Link:

    def __init__(self, v1, v2):
        self._v1 = v1
        self._v2 = v2
        self._dist = 1

    @property
    def v1(self):
        return self._v1

    @property
    def v2(self):
        return self._v2

    @property
    def dist(self):
        return self._dist

    @dist.setter
    def dist(self, value):
        self._dist = value


class LinkedGraph:

    def __init__(self):
        self._vertex = []
        self._links = []

    def add_vertex(self, v):
        self._vertex.append(v)

    def add_link(self, link):
        for i in self._links:
            if i.v1 == link.v1 and i.v2 == link.v2:
                return
            if i.v1 == link.v2 and i.v2 == link.v1:
                return
        self._links.append(link)
        self.init_graph(link)

    def init_graph(self, link):
        link.v1.links.append(link)
        link.v2.links.append(link)
        if link.v1 not in self._vertex:
            self.add_vertex(link.v1)
        if link.v2 not in self._vertex:
            self.add_vertex(link.v2)
        link.v1.init_vertex()
        link.v2.init_vertex()

    def find_path(self, start_v, stop_v):
        lst: list = self._vertex[:]
        del lst[lst.index(start_v)]
        lst.insert(0, start_v)
        N = len(lst)
        T = [math.inf] * N
        v = 0
        S = {lst[v]}
        T[v] = 0
        M = {}
        while v != -1:
            for j in lst[v].neighbour.keys():
                if j not in S:
                    w = T[v] + lst[v].neighbour[j]
                    if w < T[lst.index(j)]:
                        T[lst.index(j)] = w
                        M[lst.index(j)] = v
            v = self.arg_min(T, S)
            # print(v)
            if v >= 0:
                S.add(v)
        # print(M)
        start = 0
        end = lst.index(stop_v)
        path = [end]
        while path[-1] != start:
            path.append(M[path[-1]])
        # print(path)
        vertexes = (lst[i] for i in path[::-1])
        # print(*vertexes)
        # links = [lst[path[i]].neighbour[lst[path[i+1]]] for i in range(len(path)-1)][::-1]
        links = []
        for i in range(len(path)-1):
            for j in lst[path[i]].links:
                if j.v1 == lst[path[i+1]] or j.v2 == lst[path[i+1]]:
                    links.append(j)
        # print(*links)
        T = [tuple(vertexes), tuple(links)]
        return T

    @staticmethod
    def arg_min(T, S):
        amin = -1
        m = math.inf  # максимальное значение
        for i, t in enumerate(T):
            if t < m and i not in S:
                m = t
                amin = i

        return amin


map_graph = LinkedGraph()

v1 = Vertex()
v2 = Vertex()
v3 = Vertex()
v4 = Vertex()
v5 = Vertex()
v6 = Vertex()
v7 = Vertex()

map_graph.add_link(Link(v1, v2))
map_graph.add_link(Link(v2, v3))
map_graph.add_link(Link(v1, v3))

map_graph.add_link(Link(v4, v5))
map_graph.add_link(Link(v6, v7))

map_graph.add_link(Link(v2, v7))
map_graph.add_link(Link(v3, v4))
map_graph.add_link(Link(v5, v6))

# print(len(map_graph._links))  # 8 связей
# print(len(map_graph._vertex))  # 7 вершин
path = map_graph.find_path(v1, v6)


# print(v1.neighbour)
# print(path)
class Station(Vertex):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class LinkMetro(Link):
    def __init__(self, v1, v2, dist):
        super().__init__(v1, v2)
        self._dist = dist


map_metro = LinkedGraph()
v1 = Station("Сретенский бульвар")
v2 = Station("Тургеневская")
v3 = Station("Чистые пруды")
v4 = Station("Лубянка")
v5 = Station("Кузнецкий мост")
v6 = Station("Китай-город 1")
v7 = Station("Китай-город 2")

map_metro.add_link(LinkMetro(v1, v2, 1))
map_metro.add_link(LinkMetro(v2, v3, 1))
map_metro.add_link(LinkMetro(v1, v3, 1))

map_metro.add_link(LinkMetro(v4, v5, 1))
map_metro.add_link(LinkMetro(v6, v7, 1))

map_metro.add_link(LinkMetro(v2, v7, 5))
map_metro.add_link(LinkMetro(v3, v4, 3))
map_metro.add_link(LinkMetro(v5, v6, 3))



path = map_metro.find_path(v1, v6)
path = map_metro.find_path(v1, v6)  # от сретенского бульвара до китай-город 1
print(path[0])    # [Сретенский бульвар, Тургеневская, Китай-город 2, Китай-город 1]
print(sum([x.dist for x in path[1]]))  # 7