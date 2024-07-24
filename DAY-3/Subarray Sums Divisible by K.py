class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dp=[0]*k
        dp[0]=1
        c=0
        ans=0
        for num in nums:
            if num>0:
                c+=num
            else:
                c+=(num%k)+k
            c%=k
            ans+=dp[c]
            dp[c]+=1
        return ans
