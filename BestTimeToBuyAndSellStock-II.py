# URL : https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/submissions/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        for x in range(1,len(prices)):
            if prices[x]>prices[x-1]:
                maxProfit += prices[x] - prices[x-1]
        return maxProfit