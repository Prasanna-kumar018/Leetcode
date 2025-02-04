class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        maxi = max(nums) # to find the prime factors of all numbers
        isprime = [True]*(maxi+1)
        pf = [[] for _ in range(maxi+1)]
        for i in range(2,maxi+1):
            if isprime[i]:
                pf[i].append(i)
                for j in range(2*i,maxi+1,i):
                    isprime[j]=False
                    pf[j].append(i)
        s = set(nums)
        # print(pf)
        res = set()
        for i in range(maxi+1):
            if i in s:
                res.update(set(pf[i]))
        return len(res)