class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        n = len(nums)
        i = 0
        count = nums.count(k)
        """
        3333k333
        then modifying k is important
        """
        ans = 0
        for x in range(51):
            res  = curr = 0
            for a in nums:
                if a==k:
                    curr-=1
                if a==x:
                    curr+=1
                if curr<0:
                    curr = 0
                res = max(res,curr)
            ans = max(ans,count+res)
        return ans