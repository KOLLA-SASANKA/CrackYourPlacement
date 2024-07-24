class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP=0
        mini=float('inf')
        for i in range(len(prices)):
            mini=min(mini,prices[i])
            maxP=max(maxP,prices[i]-mini)
        return maxP
