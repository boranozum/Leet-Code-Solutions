from typing import List


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:

        list_of_tuples = [(ages[i], scores[i]) for i in range(len(scores))]

        sorted_list = sorted(list_of_tuples, key=lambda x: (x[0],x[1]))

        dp = [[-1 for i in range(len(scores))] for j in range(len(scores))]

        return self.helper(sorted_list, dp, 0, -1)

    def helper(self, sorted_list: List[tuple], dp: List[List[int]], current_player: int, prev_player: int) -> int:

        if current_player >= len(sorted_list):
            return 0

        if dp[prev_player+1][current_player] != -1:
            return dp[prev_player+1][current_player]

        if prev_player == -1 or sorted_list[current_player][1] >= sorted_list[prev_player][1]:
            dp[prev_player+1][current_player] = max(self.helper(sorted_list, dp, current_player+1, prev_player),
                                                    sorted_list[current_player][1] + self.helper(sorted_list, dp, current_player+1,
                                                                                                 current_player))
            return dp[prev_player+1][current_player]

        return self.helper(sorted_list, dp, current_player+1, prev_player)


s = Solution()
print(s.bestTeamScore([24,45,5,10,15], [1,1,1,1,1]))

