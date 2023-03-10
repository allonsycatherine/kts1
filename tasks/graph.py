from typing import Any
import collections
__all__ = (
    'Node',
    'Graph'
)
class Node:
    def __init__(self, value: Any):
        self.value = value
        self.outbound = []
        self.inbound = []

    def point_to(self, other: 'Node'):
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self):
        return f'Node({repr(self.value)})'

    __repr__ = __str__

class Graph:
    def __init__(self, root: Node):
        self._root = root
        self.visited = []
        self.visited2 = []
        self.stack = []
    def dfs(self) -> list[Node]:
        self.visited.append(self._root)
        for i in self._root.outbound:
            if i not in self.visited:
                self._root = i
                self.dfs()
        return list(self.visited)
    def bfs(self) -> list[Node]:
        queue = collections.deque([self._root])
        self.visited.append(self._root)
        while queue: 
            self._root= queue.popleft() 
            for neighbour in self._root.outbound: 
                if neighbour not in self.visited: 
                    self.visited.append(neighbour) 
                    queue.append(neighbour)
        for i in self.visited:
            if i not in self.visited2:
                self.visited2.append(i)
        return self.visited2 

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
a.point_to(b)
b.point_to(c)
c.point_to(d)
d.point_to(a)
b.point_to(d)
b.point_to(f)
f.point_to(e)
g = Graph(a)
print(g.bfs())
print(g.bfs())