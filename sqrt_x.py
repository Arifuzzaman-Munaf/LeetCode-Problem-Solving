class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        s = 0
        while s * s < x:
            s += 1

        if s * s == x:
            return s
        return s - 1


print(Solution().mySqrt(4))
