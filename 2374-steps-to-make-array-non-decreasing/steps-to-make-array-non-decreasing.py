from collections import deque
class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        n = len(nums)
        stack = []
        res = 0
        for i in range(n-1,-1,-1):
            t = 0
            while stack and stack[-1][0]<nums[i]:
                x,y = stack.pop()
                t = max(t+1,y)
            res = max(t,res)
            stack.append((nums[i],t))
        print(stack)
        return res