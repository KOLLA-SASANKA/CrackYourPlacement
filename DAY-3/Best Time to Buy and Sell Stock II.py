class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi=0
        st=prices[0]
        for i in range(0,len(prices)):
            if st < prices[i]:
                maxi+=prices[i]-st
            st=prices[i]
        return maxi
