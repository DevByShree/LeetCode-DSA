class Solution(object):
    def isValid(self, s):

        stack = []

        for key in s:

            if key == '(' or key == '[' or key == '{':
                stack.append(key)

            else:

                if not stack:
                    return False

                if key == ')' and stack[-1] == '(':
                    stack.pop()

                elif key == ']' and stack[-1] == '[':
                    stack.pop()

                elif key == '}' and stack[-1] == '{':
                    stack.pop()

                else:
                    return False

        return len(stack) == 0