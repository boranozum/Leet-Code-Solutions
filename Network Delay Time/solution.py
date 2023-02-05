from typing import List


class Node:
    def __init__(self, id):
        self.id = id
        self.neighbors = {}
        self.visited = False

class Solution:

    def dfs(self, node: Node, time: int):
        node.visited = True
        node.time = time
        for neighbor in node.neighbors:
            if not neighbor.visited or neighbor.time > time + node.neighbors[neighbor]:
                self.dfs(neighbor, time + node.neighbors[neighbor])

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        nodes = [Node(i) for i in range(1, n+1)]

        for time in times:
            nodes[time[0]-1].neighbors[nodes[time[1]-1]] = time[2]

        self.dfs(nodes[k-1], 0)

        max_time = 0
        for node in nodes:
            if not node.visited:
                return -1
            max_time = max(max_time, node.time)

        return max_time