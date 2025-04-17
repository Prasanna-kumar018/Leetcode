class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        from functools import cache
        m=len(key)
       # cache={}
        n=len(ring)
        @cache
        def func(r,k):
            if k==m:
                return 0
           # if (r,k) in cache:
           #     return cache[(r,k)]
            min_=float('inf')
            for idx,c in enumerate(ring):
                if c==key[k]:
                    ans=min(abs(idx-r),n-abs(idx-r))+1
                    x =func(idx,k+1)
                    if x!=float('inf'):
                         min_=min(min_,x+ans)
         #   cache[(r,k)]=min_
            return min_
        return func(0,0)