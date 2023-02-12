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
        self.stack = []
    def dfs(self) -> list[Node]:
        self.visited.append(self._root)
        for u in self._root.outbound:
            if u not in self.visited:
                self._root = u
                self.dfs()
        return self.visited
    def bfs(self) -> list[Node]:
        queue = collections.deque([self._root])
        self.visited.append(self._root)
        while queue: 
            vertex = queue.popleft() 
            for neighbour in self._root.outbound: 
                if neighbour not in self.visited: 
                    self.visited.append(neighbour) 
                    queue.append(neighbour)  
                    print(queue) 
        return self.visited   