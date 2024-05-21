class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1

        current_step, prev_step = 1, 1
        for i in range(n - 1):
            temp = current_step
            current_step = current_step + prev_step
            prev_step = temp

        return current_step
