class Solution:
    def rotatedDigits(self, n: int) -> int:
        s = set(['0','1','8','2','5','6','9'])
        same = set(['0','1','8'])
        count = 0
        for x in range(1,n+1):
            v = set(str(x))
            a = v - s
            if not a and (v - same):
                count+=1
        return count