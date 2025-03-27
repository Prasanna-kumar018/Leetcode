class Solution:
    def minOperations(self, grid: List[List[int]], a: int) -> int:
        res = []
        for x in grid:
            for y in x:
                res.append(y)
        res.sort()
        n = len(res)
        mid = n//2
        ans = 0
        for x in grid:
            for y in x:
                if abs(y-res[mid])%a!=0:
                    return -1
                ans += abs(y-res[mid])//a
        return ans