from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        i = 0
        while i < len(arr) - 1 and arr[i + 1] > arr[i]:
            i += 1

        if i == 0 or i + 1 == len(arr):
            return False

        while i < len(arr) - 1 and arr[i + 1] < arr[i]:
            i += 1

        return i + 1 == len(arr)


array = [0, 3, 2, 1]
print(Solution().validMountainArray(array))
