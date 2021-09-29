class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        number = {}
        for _, key in enumerate(nums):
            sub = target - key
            if sub in number:
                return sorted([_, number[sub] ])
            number[key] = _
            
