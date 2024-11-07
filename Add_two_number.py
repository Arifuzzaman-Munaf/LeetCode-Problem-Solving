# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp = ListNode()
        result = temp
        carry = 0
        while l1 or l2 or carry:
            total = carry
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            num = total % 10
            carry = total // 10
            temp.next = ListNode(num)
            temp = temp.next
        return result.next


l1 = ListNode(1)
l1.next = ListNode(8)
l2 = ListNode(0)

sol = Solution().addTwoNumbers(l1, l2)
while sol:
    print(sol.val)
    sol = sol.next
