class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        startTime = [0] + startTime + [eventTime]
        endTime = [0]+ endTime + [eventTime]
        prefix = [0]
        for x,y in zip(startTime[1:],endTime[1:]):
            prefix.append(prefix[-1]+(y-x))
        res = 0
        n = len(startTime)
        for i in range(n):
            if i+k+1>=n:
                break
            val = prefix[i+k]-prefix[i]
            total = ((startTime[i+k+1]-endTime[i])-val)
            res = max(res,total)
        return res