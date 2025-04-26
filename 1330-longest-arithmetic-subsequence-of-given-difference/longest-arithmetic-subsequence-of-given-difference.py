class Solution:
    def longestSubsequence(self, arr: List[int], diff: int) -> int:
        n = len(arr)
        d = collections.defaultdict(int)
        for idx,val in enumerate(arr):
            if val-diff in d:
                d[val]=max(d[val],d[val-diff]+1)
            
            d[val]=max(d[val],1)
        return max(d.values())