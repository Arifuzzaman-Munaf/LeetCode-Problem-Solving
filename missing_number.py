from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> float:
        n = len(nums)
        return int(n*(n+1)/2 - sum(nums))


print(Solution().missingNumber([3,0,1]))
