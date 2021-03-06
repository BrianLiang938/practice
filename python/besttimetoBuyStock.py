class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        profit = 0
        while right < len(prices):
            if prices[right] - prices[left] < 0:
                left = right
                right += 1
            elif prices[right] - prices[left] > profit:
                profit = prices[right] - prices[left]
                right += 1
            else:
                right += 1
        return profit