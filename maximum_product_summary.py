from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        left = right = 1
        max_product = max(nums)
        for i in range(len(nums)):
            left = (left, 1)[left == 0]
            right = (right, 1)[right == 0]

            left *= nums[i]
            right *= nums[len(nums) - i - 1]
            max_product = max(max_product, max(left, right))
        return max_product


print(Solution().maxProduct([2, 3, -2, 4]))
