class Solution(object):
    def makeGood(self, s):
        stack = []
        for current in s:
            if stack and abs(ord(stack[-1]) - ord(current)) == 32:
                stack.pop()
            else:
                stack.append(current)
        return "".join(stack)
