from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        a = []
        for i in range(n):
            a.append(nums[i])
            a.append(nums[n])
            n += 1

        return a


print(Solution().shuffle(nums=[2, 5, 1, 3, 4, 7], n=3))
