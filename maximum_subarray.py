from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = current_sum = nums[0]

        for i in nums[1:]:
            if current_sum < 0:
                current_sum = 0

            current_sum += i
            max_sum = max(current_sum, max_sum)

        return max_sum


print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
