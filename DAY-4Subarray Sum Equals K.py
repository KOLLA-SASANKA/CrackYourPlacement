class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res=0
        preSum=0
        d={0:1}
        for i in nums:
            preSum+=i
            if preSum - k in d:
                res+=d[preSum-k]
            if preSum not in d:
                d[preSum]=1
            else:
                d[preSum]+=1
        return res
