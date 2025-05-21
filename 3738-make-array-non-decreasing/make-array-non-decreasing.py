class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        n = len(nums)
        nge = [-1]*n
        s = []
        for idx,val in enumerate(nums):
            while s and nums[s[-1]]<=val:
                index = s.pop()
                nge[index]=idx
            s.append(idx)
        count = 0
        start = 0
        # print(nge)
        while start!=-1:
            count+=1
            start = nge[start]
        return count