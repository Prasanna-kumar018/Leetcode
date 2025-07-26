class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        yy = collections.defaultdict(int)
        for x,y in points:
            yy[y]+=1
        arr = [(x,y) for x,y in yy.items()]
        arr.sort()  
        MOD = 10**9 + 7
        ans = 0
        prev = 0
        for idx,(k,v) in enumerate(arr):
            val = (v*(v-1))//2
            if val>0:
                ans += (val*prev)
            prev+=val
        return ans%MOD
        