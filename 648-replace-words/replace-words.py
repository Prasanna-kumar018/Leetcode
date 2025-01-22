class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        class Node:
            def __init__(self):
                self.children=[None for _ in range(26)]
                self.w = None
        root = Node()
        def insert(s):
            n  = len(s)
            curr = root
            for idx,c in enumerate(s):
                a = ord(c)-ord('a')
                if not curr.children[a]:
                    curr.children[a]=Node()
                if idx == n-1:
                    curr.children[a].w=s
                curr = curr.children[a]
        
        def get(value):
            curr = root
            z = len(value)
            for idx, c in enumerate(value):
                x = ord(c)- ord('a')
                if  not curr.children[x]:
                    return ''
                if curr.children[x].w:
                    return curr.children[x].w
                curr = curr.children[x] 
            return ''

        l = sentence.strip().split(' ')
        for s in dictionary:
            insert(s)
        for idx,value in enumerate(l):
            x = ord(value[0])-ord('a')
            if  root.children[x]:
                z = get(value)
                l[idx]=(z if z!='' else value )

        return ' '.join(l)
            