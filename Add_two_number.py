# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode :
        result = []
        for i in range(len(l1)):
            result.append(l1[i] + l2[i])
            
        print(result)


Solution().addTwoNumbers([1,2,3], [2,3,4])