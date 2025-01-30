class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curr = 0
        mini = 0
        total = sum(nums)
        res = float('-inf')
        minisubarray = float('inf')
        for idx,x in enumerate(nums):
            curr+=x
            res = max(res,curr)
            if curr<0:
                curr=0

            mini +=x
            minisubarray = min(mini,minisubarray)
            if mini>0:
                mini=0
        # print(res,minisubarray)
        if total == minisubarray:
            return res
        return max(res,total-minisubarray)