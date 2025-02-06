class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        class Node:
            def __init__(self):
                self.children=[None]*10
            def __str__(self):
                res = [x for x in self.children]
                return str(res)
        root=Node()
        def insert(string):
            curr=root
            for c in string:
                idx = ord(c)-ord('0')
                if not curr.children[idx]:
                    curr.children[idx]=Node()
                curr=curr.children[idx]

        def search(string):
            s = 0
            curr=root
            for c in string:
                idx = ord(c) - ord('0')
                if not curr.children[idx]:
                    break
                curr=curr.children[idx]
                s+=1
            return s
        for x in arr1:
            insert(str(x))
        
        res = 0
        for  x in arr2:
            res = max(res,search(str(x)))
        return res