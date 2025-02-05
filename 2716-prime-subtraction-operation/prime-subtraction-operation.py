import bisect
class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        n = len(nums)
        maxi = max(nums)
        s = []
        isPrimes = [True]*(maxi+1)
        isPrimes[0]=isPrimes[1]=False
        for i in range(2,maxi+1):
            if isPrimes[i]:
                s.append(i)
                for x in range(2*i,maxi+1,i):
                    isPrimes[x]=False
        # print(s)
        s.sort()
        value = bisect.bisect_left(s,nums[0])-1
        prev= nums[0]
        if value>=0:
            prev = min(prev,nums[0]-s[value])
        print(prev)
        for i in range(1,n):
            if nums[i]<=prev:
                return False
            diff = nums[i]-prev
            idx = bisect.bisect_left(s,diff)-1
            if idx>=0:
                prev = nums[i]-s[idx]
            else:
                prev = nums[i]
            print(prev)
        return True
