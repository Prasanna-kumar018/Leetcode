class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        M = max(2,max(nums)+1)
        primes = [True]*M
        primes[0]=primes[1]=False
        count = [0]*M
        for x in range(2,M):
            if primes[x]:
                for j in range(x,M,x): # start from x to make the count of x incre by 1
                    primes[j]=False
                    count[j]+=1
        q = []
        def push(val):
            heapq.heappush(q,val)
        def pop():
            return heapq.heappop(q)
        
        for idx,val in enumerate(nums):
            push((-val,-count[val],idx))
        pgee = [-1]*n
        nge = [n]*n
        s = []
        for idx,val in enumerate(nums):
            while s and count[s[-1][0]]<count[val]:
                _,ind = s.pop()
                nge[ind] = idx 
            s.append((val,idx))
        s = []
        for idx in range(n-1,-1,-1):
            val = nums[idx]
            while s and count[s[-1][0]]<=count[val]:
                _, ind = s.pop()
                pgee[ind]=idx
            s.append((val,idx))
    
        total = 1
        # print(nums)
        # print([count[x] for x in nums])
        # print(nge)
        # print(pgee)
        while k>0 and q:
            cc , _ , index = pop()
            left = index-pgee[index]
            right = nge[index]-index
            # print(left,right,index,cc)
            c = min(k,left*right)
            total *= pow(nums[index],c,MOD)
            total %= MOD
            k-=c
        return total % MOD