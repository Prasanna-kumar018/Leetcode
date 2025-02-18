class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        vis = set()
        def recur(mask,res):
            if res not in vis and res!='':
                vis.add(res)
            for idx,val in enumerate(tiles):
                if (mask&(1<<idx))==0:
                    recur(mask|(1<<idx),res+val)
        recur(0,'')
        return len(vis)