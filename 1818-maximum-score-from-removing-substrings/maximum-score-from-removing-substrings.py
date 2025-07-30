class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:

        ans = 0
        if y>=x:
            st = []
            for idx,val in enumerate(s):
                if st and s[st[-1]]=='b' and val=='a':
                    st.pop()
                    ans+=y
                else:
                    st.append(idx)
            st2 = []
            for idx,val in enumerate(st):
                if st2 and s[st2[-1]]=='a' and s[val]=='b':
                    st2.pop()
                    ans+=x
                else:
                    st2.append(val)
        else:
            st = []
            for idx,val in enumerate(s):
                if st and s[st[-1]]=='a' and val=='b':
                    st.pop()
                    ans+=x
                else:
                    st.append(idx)
            st2 = []
            for idx,val in enumerate(st):
                if st2 and s[st2[-1]]=='b' and s[val]=='a':
                    st2.pop()
                    ans+=y
                else:
                    st2.append(val)
        return ans