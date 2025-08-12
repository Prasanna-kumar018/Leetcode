class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        """
        t = 4
start   = - - - - + +
        - = - - - + +
        - - = - - + +
        - - - = - + +
        - - - - = + + (end)
        + + + + + + +
        + + + + + + +
        here when t = 4 all the minus - and = equalto symbols can be covered...
        but + symbols can't be covered as it's x or y distance is greater than t 
        """
        xx = abs(sx-fx) 
        yy = abs(sy-fy)
        if sx==fx and sy==fy:
            return t!=1 # because 2 and 3 can make any step greater than one
        """
        ---> 2 steps cycle
        <---

        <---
        \   /|\    
         \   |   
          \  |  3 steps cycle
          _\||
        """
        return xx<=t and yy<=t