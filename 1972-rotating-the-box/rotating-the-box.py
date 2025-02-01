class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m = len(box)
        n = len(box[0])
        for i in range(m):
            count = 0
            for j in range(n):
                if box[i][j]=='#':
                    count+=1
                elif box[i][j]=='*' and count>0:
                    box[i][j-count]='$'
                    count=0
            if count>0:
                box[i][n-count]='$'
            start = False
            print(box[i])
            for j in range(n):
                if box[i][j]=='*':
                    start = False
                    continue
                if box[i][j]=='$':
                    start = True
                if start:
                    box[i][j]='#'
                else:
                    box[i][j]='.'
            print(box[i])
        return [list(col) for col in zip(*box[::-1])]