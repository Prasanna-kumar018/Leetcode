class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        startTime= [0]+ startTime + [eventTime]
        endTime = [0] + endTime + [eventTime]
        prefix = [0]
        for x,y in zip(startTime[1:],endTime[1:]):
            prefix.append(prefix[-1]+(y-x))
        n = len(startTime)
        prefixm = [0]*n
        for i in range(1,n):
            prefixm[i]=max(prefixm[i-1],(startTime[i]-endTime[i-1]))
        suffixm = [0]*n
        for i in range(n-2,-1,-1):
            suffixm[i]=max(suffixm[i+1],(startTime[i+1]-endTime[i]))
        k = 1 
        res = 0
        for i in range(n):
            if i+k+1>=n:
                break
            val = (prefix[i+k]-prefix[i])
            if max(prefixm[i],suffixm[i+k+1])>=val:
                val = 0
            total = (startTime[i+k+1]-endTime[i])-val
            # print(total,val,i,prefixm[i],suffixm[i+1])
            res = max(res,total)
        return res