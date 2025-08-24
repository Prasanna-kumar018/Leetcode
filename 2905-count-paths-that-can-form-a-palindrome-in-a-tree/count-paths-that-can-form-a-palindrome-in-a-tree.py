class Solution:
    def countPalindromePaths(self, parent: List[int], s: str) -> int:
        g = collections.defaultdict(list)
        for idx,node in enumerate(parent):
            g[node].append((idx,ord(s[idx])-ord('a')))
        total = 0
        counter = collections.Counter()
        def go(node,mask):
            nonlocal total
            total += counter[mask]
            for i in range(26):
                total += counter[mask^(1<<i)]
            
            counter[mask]+=1
            for des,c in g[node]:
                go(des,mask^(1<<c))
        go(0,0)
        return total