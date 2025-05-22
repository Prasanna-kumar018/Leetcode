class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        if n<=2:
            return n
        x = int(math.floor(math.log2(n)))+1
        return pow(2,x)