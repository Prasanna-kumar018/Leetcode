class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        
        val = 0
        res = 0
        for idx,x in enumerate(target):
            prev = (target[idx-1] if idx-1>=0 else 0)
            if prev<x:
                res+=(x-prev)
        return res
