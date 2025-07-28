class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        n = len(s)
        d = collections.defaultdict(int)
        st = []
        for idx,val in enumerate(s):
            if st and s[st[-1]]=='(' and val==')':
                ind = st.pop()
                print(ind)
                if idx-1>ind:
                    d[idx]=2*d[idx-1]
                if idx-ind == 1:
                    d[idx] = 1
                d[idx]+=d[ind-1]
            else:
                st.append(idx)
            print(d)
        return d[max(d.keys())]