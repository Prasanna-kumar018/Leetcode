class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        v = 0
        cnt = 1
        for x in s:
            v = (v*10) + (ord(x)-ord('0'))
            if v>k:
                v = ord(x)-ord('0') 
                cnt +=1
            if v>k:
                return -1
        return cnt