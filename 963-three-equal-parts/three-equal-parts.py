class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ones = arr.count(1)
        if ones%3!=0:
            return [-1,-1]
        if ones==0:
            return [0,n-1]
        part = ones//3
        demo = []
        count = 0
        idx = arr.index(1)
        for idx,x in enumerate(arr[idx:],idx):
            if x==1:
                if count % part == 0:
                    demo.append([])
                count+=1
            demo[-1].append((x,idx))
        ans = [-1,-1]
        length = len(demo[2])
        for i in range(length):
            if i==len(demo[1]) or i==len(demo[0]):
                return [-1,-1]
            x,y,z = demo[0][i],demo[1][i],demo[2][i]
            if x[0]!=y[0] or y[0]!=z[0] or z[0]!=x[0]:
                return [-1,-1]
            if i==length-1: 
                ans= [x[1],y[1]+1]
                break
        return ans