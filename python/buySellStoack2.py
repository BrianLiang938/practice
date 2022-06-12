class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prev = prices[0]
        out = 0
        for num in prices:
            if num > prev:
                out += num - prev
            prev = num
        return out
