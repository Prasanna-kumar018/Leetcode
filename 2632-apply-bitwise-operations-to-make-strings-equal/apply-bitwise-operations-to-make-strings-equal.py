class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        """
        0 0 0 0
        0 1 1 1
        1 0 1 1
        1 1 1 0

        0 -> 1 after 1 or before 1
        1 -> 0 before 1 
        """
        if s==target:
            return True
        return s.count('1') > 0 and target.count('1') > 0