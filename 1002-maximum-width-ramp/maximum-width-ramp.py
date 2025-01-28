class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        res = [(val,idx) for idx,val in enumerate(nums)]
        res.sort()
        mini = res[0][1]
        result = 0
        for val,idx in res[1:]:
            if mini <idx:
                result = max(result,idx-mini)
            mini=min(mini,idx)
        return result