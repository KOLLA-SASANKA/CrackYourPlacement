from typing import List

class Solution:
    def findPair(self, n : int, x : int, arr : List[int]) -> int:
        # code here
        p=set()
        for i in arr:
            if (i+x) in p or (i-x) in p:
                return 1
            p.add(i)
        return -1
