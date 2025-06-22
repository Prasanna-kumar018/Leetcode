class Solution:
    def primeSubarray(self, nums: List[int], k: int) -> int:
        n = max(nums)
        isprime = [True]*(n+1)
        isprime[0]=False
        isprime[1]=False
        for i in range(2,n+1):
            if isprime[i]:
                for j in range(2*i,n+1,i):
                    isprime[j]=False
        M = len(nums)
        # print(isprime)
        minq = collections.deque()
        maxq = collections.deque()
        left = 0
        q = collections.deque()
        ans = 0
        for right in range(M):
            if isprime[nums[right]]:
                q.append(right)
                while minq and nums[right]< minq[-1][0]:
                    minq.pop()
                minq.append((nums[right],right))
                while maxq and nums[right]> maxq[-1][0]:
                    maxq.pop()
                maxq.append((nums[right],right))
                while maxq and minq and maxq[0][0]-minq[0][0] >k:
                    if maxq[0][1]==left:
                        maxq.popleft()
                    if minq[0][1]==left:
                        minq.popleft()
                    if q[0]==left:
                        q.popleft()
                    left+=1
            if len(q)<2:
                continue
        # q contains only the prime indices , we have to take the index just before the last one
            ans += q[-2]-left+1  
        return ans
