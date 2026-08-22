class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        max_p = 0
        while i < len(prices):
            for p in range(i + 1, len(prices)):
                if prices[i] >= prices[p]:
                    continue
                else:
                    profit = prices[p] - prices[i]
                    if profit > max_p:
                        max_p = profit
            i += 1

        return max_p