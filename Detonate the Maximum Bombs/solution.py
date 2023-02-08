from typing import List


class Bomb:
    def __init__(self, x: int, y:int, r:int):
        self.x = x
        self.y = y
        self.r = r
        self.inRange = []

    def isInRange(self, b):
        return (self.x - b.x)**2 + (self.y - b.y)**2 <= self.r**2



class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:

        for i in range(len(bombs)):
            bombs[i] = Bomb(bombs[i][0], bombs[i][1], bombs[i][2])

        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i != j and bombs[i].isInRange(bombs[j]):
                    bombs[i].inRange.append(j)

        # run dfs for each bomb
        maxDetonation = 0
        for i in range(len(bombs)):
            visited = [False for i in range(len(bombs))]
            visited[i] = True
            self.dfs(bombs, i, visited)
            maxDetonation = max(maxDetonation, sum(visited))

        return maxDetonation

    def dfs(self, bombs, i, visited):
        for j in bombs[i].inRange:
            if not visited[j]:
                visited[j] = True
                self.dfs(bombs, j, visited)

s = Solution()
print(s.maximumDetonation([[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]))
