class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        l=set()
        res=[]
        for i in nums:
            if i in l:
                res.append(i)
            else:
                l.add(i)
        return res
                
