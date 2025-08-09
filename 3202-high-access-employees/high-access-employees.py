class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        d = collections.defaultdict(list)
        for x,y in access_times:
            d[x].append(y)
        for x,y in d.items():
            y.sort()
        ans = []
        for x in d:
            n = len(d[x])
            res = False
            for idx in range(n):
                if idx+2<n:
                    vv = int(d[x][idx+2][-2:])-int(d[x][idx][-2:])
                    xx = (int(d[x][idx+2][:-2])-int(d[x][idx][:-2]))*60
                    xx +=vv
                    if xx<=59:
                        res = True
            if res:
                ans.append(x)
        return ans
        
