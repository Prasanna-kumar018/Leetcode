class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:

        """
    [
        [1,  1,  4,  1],
        [10 ,8, 13, 17],
        [2 , 12, 1,  16]]
        """
        R = len(image)
        C = len(image[0])
        L = 3
        dp = [[0]*C for _ in range(R)]
        result = [[0]*C for _ in range(R)]
        for i in range(R):
            for j in range(C):
                if i+L <= R and j+L <=C:
                    res = True
                    s = 0
                    for r in range(L):
                        for c in range(L):
                            xx = r+i
                            yy = c+j
                            s += image[xx][yy]
                            if xx+1<i+L:
                                if abs(image[xx+1][yy]-image[xx][yy])>threshold:
                                    res = False
                            if yy+1<j+L:
                                if abs(image[xx][yy+1]-image[xx][yy])>threshold:
                                    res = False
                    # print(i,j,s//9,dp[i][j],"outside",res)
                    if res:
                        avg = s // 9
                        dp[i][j]+=1
                        # print(i,j,avg,dp[i][j])
                        result[i][j]=avg
        def go(arr):
            RR = len(arr)
            CC = len(arr[0])
            for i in range(RR):
                for j in range(1,CC):
                    arr[i][j]+=arr[i][j-1]
            for j in range(CC):
                for i in range(1,RR):
                    arr[i][j]+=arr[i-1][j]
        go(dp)
        go(result)
        def get(arr,sx,sy,ex,ey):
            return arr[ex][ey]-(arr[ex][sy-1] if sy-1>=0 else 0)- (arr[sx-1][ey] if sx-1>=0 else 0) + (arr[sx-1][sy-1] if sx-1>=0 and sy-1>=0 else 0)


        for i in range(R):
            for j in range(C):
                count = get(dp,max(0,i-2),max(0,j-2),i,j)
                avg  = get(result,max(0,i-2),max(0,j-2),i,j)
                if count!=0:
                    image[i][j]=avg//count
        return image
        