class Solution(object):
    def removeDuplicates(self, s):

        stack = []

        for current in s:

            if stack and current == stack[-1]:
                stack.pop()
            else:
                stack.append(current)
        return ''.join(stack)