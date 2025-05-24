class Solution:
    def stringSequence(self, target: str) -> List[str]:
        res = []
        add = ''
        n = len(target)
        for  i in range(n):
            ind = 0
            while target[i] != chr(97+ind):
                res.append(add+chr(97+ind))
                ind+=1
            res.append(add+chr(97+ind))
            add+=target[i]
        return res