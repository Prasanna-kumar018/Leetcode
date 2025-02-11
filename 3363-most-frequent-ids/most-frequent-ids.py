class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        q = []
        def push(val):
            heapq.heappush(q,val)
        def pop():
            return heapq.heappop(q)
        ans = []
        d = collections.defaultdict(int)
        remove = collections.defaultdict(int)
        for x,c in zip(nums,freq):
            remove[d[x]]+=1
            push(-(d[x]+c))
            d[x]=d[x]+c
            while q and remove[abs(q[0])]>0:
                a = abs(pop())
                remove[a]-=1
            if q: 
                ans.append(abs(q[0]))
            else:
                ans.append(0)
        return ans
