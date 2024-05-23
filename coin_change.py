from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        res = [float('inf')] * (amount + 1)
        res[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    res[i] = min(res[i], res[i - coin] + 1)
        return (res[-1], -1)[res[-1] == float('inf')]


print(Solution().coinChange([1, 2, 5], 11))
