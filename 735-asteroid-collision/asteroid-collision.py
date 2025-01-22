class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []
        for x in asteroids:
            push = True
            while s and (s[-1]>0 and x<0 ):
                val = s.pop()
                if abs(val)==abs(x):
                    push=False
                    break
                if abs(val)>abs(x):
                    s.append(val)
                    push = False
                    break
            if push:
                s.append(x)
        return s