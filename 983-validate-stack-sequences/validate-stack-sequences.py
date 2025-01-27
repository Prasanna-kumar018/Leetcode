class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        n= len(popped)
        s=[]
        i = 0
        for c in pushed:
            s.append(c)
            while s and i<n and  s[-1]==popped[i]:
                s.pop()
                i+=1
        return True if i==n and  not s else False
        