from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        max_profit = 0

        for right, price in enumerate(prices):
            if prices[left] < price:
                max_profit = max(max_profit, price - prices[left])
            else:
                left = right
        return max_profit


print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
