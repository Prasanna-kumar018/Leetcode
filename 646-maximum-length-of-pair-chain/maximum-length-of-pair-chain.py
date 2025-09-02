class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        n = len(pairs)
        pairs.sort(key = lambda x : x[1])
        start = 1 
        prev = pairs[0]
        for x in pairs[1:]:
            if x[0]>prev[1]:
                prev = x
                start += 1 
        return start