class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        l = []
        for idx,val in enumerate(nums):
            heapq.heappush(l,(val,idx))
        s = sum(nums)
        res = []
        vis= set() # contains idx
        for x,y in queries:
            t= y
            if x not in vis:
                vis.add(x)
                s-=nums[x]    
            while t>0 and l:
                val,idx = heapq.heappop(l)
                if idx in vis:
                    t+=1
                else:
                    s-=val
                    vis.add(idx)
                t-=1
         #   print(s,l)
            res.append(s)
        return res
            