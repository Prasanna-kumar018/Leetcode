class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        d = collections.defaultdict(int)
        for x in nums:
            d[x] = 1
        for x,y in zip(moveFrom,moveTo):
            d[y] = 1
            if x!=y:
                d[x] = 0
        res = []
        for x in sorted(d.keys()):
            for _ in range(d[x]):
                res.append(x)
        return res