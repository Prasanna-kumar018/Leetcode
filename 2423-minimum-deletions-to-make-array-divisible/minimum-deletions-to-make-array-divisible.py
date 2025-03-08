class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        g = 0
        for x in numsDivide:
            g = math.gcd(g,x)
        nums.sort()
        for idx,val in enumerate(nums):
            if g%val==0:
                return idx
        return -1