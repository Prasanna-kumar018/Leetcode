class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        count = 0
        gx,gy = collections.defaultdict(list),collections.defaultdict(list)
        for x,y in buildings:
            gx[x].append(y)
            gy[y].append(x)
        for x,y in gx.items():
            y.sort()
        for x,y in gy.items():
            y.sort()
        
        for x,y in buildings:
            idx1 = bisect.bisect_right(gx[x],y)
            idx2 = bisect.bisect_left(gx[x],y)-1
            idx3 = bisect.bisect_right(gy[y],x)
            idx4 = bisect.bisect_left(gy[y],x)-1
            if 0<= idx1 <len(gx[x]) and 0<=idx2<len(gx[x]) and 0<=idx3 <len(gy[y]) and 0<= idx4 <len(gy[y]):
                count+=1
        return count