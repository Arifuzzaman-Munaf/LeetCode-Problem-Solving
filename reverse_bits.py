class Solution:
    def reverseBits(self, n: int):
        n = bin(n).replace("0b", "")
        return int(("0" * (32 - len(n)) + n)[::-1], 2)
