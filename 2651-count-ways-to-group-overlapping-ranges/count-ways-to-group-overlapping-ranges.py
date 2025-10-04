class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        ranges.sort()
        arr = [ranges[0]]
        prev = ranges[0]
        MOD = 10**9 + 7
        for x,y in ranges[1:]:
            if x<=prev[1]:
                prev[1]=max(prev[1],y)
            else:
                prev = [x,y]
                arr.append(prev)
        return (2**len(arr)) % MOD