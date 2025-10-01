class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        c = collections.defaultdict(list)
        for idx,val in enumerate(nums):
            c[val].append(idx)
        for x,y in c.items():
            y.sort()
        n = len(nums)
        ans = [0]*n
        for x,y in c.items():
            s = 0
            for idx,xx in enumerate(y):
                ans[xx] += (idx*xx)-s
                s += xx
            s = 0
            for idx,xx in enumerate(y[::-1]):
                ans[xx] += s-(idx*xx)
                s += xx
        return ans