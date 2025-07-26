class Solution:
    def processStr(self, s: str) -> str:
        stack = []

        for x in s:
            if x.isalpha():
                stack.append(x)
            elif x=='*' and stack:
                stack.pop()
            elif x=='#':
                stack = stack + stack
            elif x=='%':
                stack.reverse()
        return ''.join(stack)
