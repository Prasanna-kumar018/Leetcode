class Solution:
    def minOperations(self, nums: List[int]) -> int:
        s = []
        res = 0
        nums.append(0)
        for idx,val in enumerate(nums):
            while s and nums[s[-1]]>val:
                x = s.pop()
                res += 1
                while s  and nums[x]==nums[s[-1]]:
                    s.pop()
            s.append(idx)
            # print(s)
        return res