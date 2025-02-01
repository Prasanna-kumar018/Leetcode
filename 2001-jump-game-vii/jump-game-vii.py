class Solution:
  def canReach(self,s: str, minJump: int, maxJump: int) -> bool:
        if s[-1]=='1':
            return False
        l = [[minJump,maxJump]]
        idx = 0
        n = len(s)
        for i, c in enumerate(s):
            while idx<len(l) and i > l[idx][1]:
                idx = idx +1 
            if idx == len(l):
                return False
            if c == '0' and l[idx][0] <=  i  <= l[idx][1]:
                if i==n-1:
                    return True
                l.append([i+minJump,i+maxJump])
        return False