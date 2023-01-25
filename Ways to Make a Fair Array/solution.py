from typing import List

class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:

        current_counts = [(nums[0],0)]
        number_of_indices = 0

        for i in range(1, len(nums)):

            if i % 2 != 0:
                new_count = (current_counts[i-1][0], nums[i]+current_counts[i-1][1])
                current_counts.append(new_count)

            else:
                new_count = (nums[i] + current_counts[i - 1][0], current_counts[i - 1][1])
                current_counts.append(new_count)

        reverse_counts = [(0,0) for i in range(len(nums))]

        if len(nums) % 2 == 0:
            reverse_counts[-1] = (0, nums[-1])
        else:
            reverse_counts[-1] = (nums[-1], 0)

        for i in range(len(nums)-2, -1, -1):
            if i % 2 != 0:
                new_count = (reverse_counts[i + 1][0], nums[i] + reverse_counts[i + 1][1])
                reverse_counts[i] = new_count

            else:
                new_count = (nums[i] + reverse_counts[i + 1][0], reverse_counts[i + 1][1])
                reverse_counts[i] = new_count

        for i in range(len(nums)):
            if i == 0:
                if reverse_counts[i+1][0] == reverse_counts[i+1][1]:
                    number_of_indices+=1
            elif i == len(nums)-1:
                if current_counts[i-1][0] == current_counts[i-1][1]:
                    number_of_indices+=1
            elif i % 2 != 0:
                if current_counts[i][0] + reverse_counts[i+1][1] == current_counts[i][1]-nums[i]+reverse_counts[i+1][0]:
                    number_of_indices+=1

            else:
                if current_counts[i][0] - nums[i] + reverse_counts[i + 1][1] == current_counts[i][1] + reverse_counts[i+1][0]:
                    number_of_indices += 1

        return number_of_indices


