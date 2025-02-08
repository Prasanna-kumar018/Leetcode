class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        time = 0
        d = {}
        for x in tasks:
            if x not in d:
                d[x]=time
            else:
                if time-d[x]<space+1:
                    time=d[x]+space+1
                d[x]=time
            time+=1
            # print(time)
        return time