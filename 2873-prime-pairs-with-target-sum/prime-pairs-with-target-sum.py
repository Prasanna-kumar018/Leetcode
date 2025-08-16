class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        N = max(2,n)
        isprime = [True for _ in range(N+1)]
        isprime[0]=False
        isprime[1]=False
        res = set()
        ans = []
        for i in range(2,n+1):
            if isprime[i]:
                res.add(i)
                if n-i in res:
                    ans.append([n-i,i])
                for j in range(2*i,n+1,i):
                    isprime[j]=False
        ans.reverse()
        return ans