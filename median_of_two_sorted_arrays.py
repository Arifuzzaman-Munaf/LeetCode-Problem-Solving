import math
from typing import List


def median(array):
    if len(array) % 2 == 0:
        return (array[len(array) // 2] + array[len(array) // 2 - 1]) / 2
    return array[len(array) // 2]


class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return median(sorted(nums1 + nums2))


print(Solution().findMedianSortedArrays([1, 2], [3, 4]))

print(Solution().findMedianSortedArrays([1, 2, 5], [3, 4]))
