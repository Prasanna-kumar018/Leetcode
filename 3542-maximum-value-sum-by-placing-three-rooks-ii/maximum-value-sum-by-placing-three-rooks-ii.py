class Solution:
    def maximumValueSum(self, board: List[List[int]]) -> int:
        R = len(board)
        C = len(board[0])
        
        new_board = []
        for x in board:
            new_board.append(sorted([(val,idx) for idx,val in enumerate(x)],reverse=True)[:3])
        
        def preprocess(new_board):
            top = []
            current = []
            for x in new_board:
                current.extend(x)
                current = sorted(current,reverse=True)
                seen = set()
                nxt = []
                for val,idx in current:
                    if idx not in seen:
                        seen.add(idx)
                        nxt.append((val,idx))
                    if len(nxt)==3:
                        break
                top.append(nxt) 
            return top
        top = preprocess(new_board)
        bottom = preprocess(new_board[::-1])[::-1]
        best = float('-inf')
        for i in range(1,R-1):
            for main,c in new_board[i]:
                for x1,c1 in top[i-1]:
                    for x2,c2 in bottom[i+1]:
                        if c!=c1 and c1!=c2 and c2!=c:
                            best = max(best,x1+x2+main)
                    
        return best
    