MAXI = 10**6
arr = [ x for x in range(MAXI+1)]
for x in range(2,MAXI+1):
    j = 2*x
    while j<=MAXI:
        arr[j]=x
        j+=x
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        INF = 10**20
        count = 0
        for i in range(n-2,-1,-1):
            while nums[i]>nums[i+1] and arr[nums[i]]!=nums[i]:
                nums[i] //= arr[nums[i]]
                count += 1
            if nums[i]>nums[i+1]:
                return -1
        return count