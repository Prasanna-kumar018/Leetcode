class Solution:
    def maxArea(self, coords: List[List[int]]) -> int:
        area = 0
        xx = collections.defaultdict(list)
        yy = collections.defaultdict(list)
        INF = 10**20
        maxx,maxy,minx,miny= -INF,-INF,INF,INF
        for x,y in coords:
            xx[y].append(x)
            yy[x].append(y)
            maxx = max(maxx,x)
            minx = min(minx,x)
            maxy = max(maxy,y)
            miny = min(miny,y)
        for x,y in xx.items():
            y.sort()
        for x,y in yy.items():
            y.sort()
        # print(xx,yy)
        for x,y in xx.items():
            if len(y)>=2:
                start , end = y[0],y[-1]
                L = end-start
                print(L,max(abs(x-maxy),abs(x-miny)),x)
                area = max(area, L*max(abs(x-maxy),abs(x-miny)))
        for x,y in yy.items():
            if len(y)>=2:
                start , end = y[0],y[-1]
                L = end-start
                area = max(area, L*max(abs(x-maxx),abs(x-minx)))
        return area if area!=0 else -1