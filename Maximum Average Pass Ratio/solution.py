from typing import List


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:

        pass_ratios = []
        avg_ratio = 0
        for i in range(len(classes)):
            current_pass_ratio = float(classes[i][0] / classes[i][1])
            profit = float((classes[i][0] + 1) / (classes[i][1] + 1)) - current_pass_ratio
            pass_ratios.append((profit,i))
            avg_ratio += current_pass_ratio

        avg_ratio /= len(classes)
        pass_ratios = sorted(pass_ratios, key=lambda x: x[0], reverse=True)

        while extraStudents > 0:
            profit, index = pass_ratios[0]
            classes[index][0] += 1
            classes[index][1] += 1
            avg_ratio += profit/len(classes)
            new_profit = float((classes[index][0] + 1) / (classes[index][1] + 1)) - float(classes[index][0] / classes[index][1])
            pass_ratios[0] = (new_profit, index)
            pass_ratios = sorted(pass_ratios, key=lambda x: x[0], reverse=True)
            extraStudents -= 1

        return avg_ratio


s = Solution()
print(s.maxAverageRatio([[2,4],[3,9],[4,5],[2,10]], 4))