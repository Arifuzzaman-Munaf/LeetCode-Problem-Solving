from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if nums and len(nums) < 3:
            return []
        nums.sort()
        triplets = set()
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                current_triplets = (nums[i], nums[left], nums[right])
                sum_triplets = sum(current_triplets)
                if sum_triplets == 0:
                    triplets.add([i, left, right])
                    left += 1
                    right -= 1
                elif sum_triplets < 0:
                    left += 1
                else:
                    right -= 1
        return triplets
