class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        v = 0
        N = len(nums)
        count = [0]*N
        for idx,val in enumerate(nums):
            v += count[idx]
            if v < val:
                d = val-v
                if idx+k<N:
                    count[idx+k]-=d
                elif idx+k>N:
                    return False
                v += d
            elif v>val:
                return False
        return True