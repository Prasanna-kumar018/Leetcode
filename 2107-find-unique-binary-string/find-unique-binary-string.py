class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        vis = set(nums)
        maxi = n
        for i in range(2**n):
            b = bin(i)[2:]
            b = '0'*(maxi-len(b))+b
            if b not in vis:
                return b
        return ''