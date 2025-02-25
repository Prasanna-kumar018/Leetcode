class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        tasks = set(tuple(x) for x in tasks)
        events = []
        for index,(s,e,d) in enumerate(tasks):
            events.append((s,-1,d,index)) # -1-start
            events.append((e,1,d,index))
        events.sort()
        current = {}
        ans = 0
        for x,token,d,index in events:
            if token==-1: # if start and end are same coz of -1 start will come first
                current[index]=[x,d]
                # print(current)
            else:
                ans += current[index][1] # for this only index is set in start and end
                value = current[index][1]
                for idx in current.keys():
                    s,dur = current[idx]
                    t = value
                    # print(t,x-s+1)
                    if x-s+1 < t:
                        t = x-s+1
                    current[idx][0]+=t
                    current[idx][1]-=t
                    current[idx][1]=max(current[idx][1],0)
                # print(ans)
                # print(current)
        return ans
