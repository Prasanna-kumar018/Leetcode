class Solution:
    def findPermutation(self, nums: List[int]) -> List[int]:
        INF = 10**20
        n = len(nums)
        data = collections.defaultdict(lambda :collections.defaultdict(lambda :collections.defaultdict(int)))
        @cache
        def recur(s,prev,mask):
            if mask == ((1<<n)-1):
                return abs(prev-nums[s])
            best = INF
            for i in range(n):
                if (mask & (1<<i) )==0:
                    x = abs(prev-nums[i])+recur(s,i,mask|(1<<i))
                    if x<best:
                        best = min(best,x)
                        # data[(s,prev,mask)] = (s,i,mask|(1<<i))
                        data[s][prev][mask] = i
            return best
        sp,sm = -1,-1
        res = recur(0,0,(1<<0))
        sp = 0
        sm = (1<<0)
        ss = sp
        res = [sp]
        while len(res)<n:
            np = data[ss][sp][sm]
            res.append(np)
            sp ,sm = np,sm|(1<<np)
        return res
        
