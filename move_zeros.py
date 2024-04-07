from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for num in nums:
            if num != 0:
                nums[j] = num
                j += 1

        nums[j:] = [0] * (len(nums) - j)


solution = Solution()
numbers = [0, 1, 0, 3, 12]
solution.moveZeroes(numbers)
print(numbers)
