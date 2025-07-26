class Solution:
    def splitArray(self, nums: List[int]) -> int:
        a = 0
        b = 0
        N = len(nums)
        N = max(2,N)
        isprime = [True]*N
        isprime[0]=False
        isprime[1]=False
        for i in range(2,N):
            if isprime[i]:
                for j in range(2*i,N,i):
                    isprime[j]=False
        
        for idx,val in enumerate(nums):
            if isprime[idx]:
                a += val
            else:
                b += val
        return abs(a-b)
