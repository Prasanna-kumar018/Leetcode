class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def func(x):
            if x[-1].isdigit():
                return (1,)
            s = x.split(" ")
            return (0,' '.join(s[1:]),s[0])

        logs.sort(key=func)
        return logs