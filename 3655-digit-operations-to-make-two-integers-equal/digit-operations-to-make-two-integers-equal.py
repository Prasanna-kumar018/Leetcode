class Solution:
    def minOperations(self, n: int, m: int) -> int:
        INF = 10**20
        dis= collections.defaultdict(lambda : INF)
        MX = 10**4
        isprime = [True]*max(2,MX)
        isprime[0]=False
        isprime[1]=False
        for i in range(2,MX):
            if isprime[i]:
                for j in range(2*i,MX,i):
                    isprime[j]=False
        q = []
        if isprime[n]:
            return -1
        def push(val):
            heapq.heappush(q,val)
        def pop():
            return heapq.heappop(q)
        push((n,n))
        dis[n]=n
        L = len(str(m))
        while q:
            val, node = pop()
            if m == node:
                return val
            if dis[node]<val:
                continue
            s = str(node).zfill(L)
            for i in range(L):
                if s[i]!='9':
                    nxt = node + pow(10,L-1-i)
                    if not isprime[nxt] and dis[nxt]>dis[node]+nxt:
                        dis[nxt]=dis[node]+nxt
                        push((dis[nxt],nxt))
                if i!=0 and s[i]!='0':
                    nxt = node - pow(10,L-1-i)
                    if not isprime[nxt] and dis[nxt]>dis[node]+nxt:
                        dis[nxt]=dis[node]+nxt
                        push((dis[nxt],nxt))
                if i==0  and s[i] > '1':
                    nxt = node - pow(10,L-1-i)
                    if not isprime[nxt] and dis[nxt]>dis[node]+nxt:
                        dis[nxt]=dis[node]+nxt
                        push((dis[nxt],nxt))
            # print(q)
        return dis[m] if dis[m]!=INF else -1
