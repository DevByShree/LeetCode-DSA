class Solution(object):
    def isValid(self, s):
        stack = []

        for ch in s:

            if ch =='(' or ch =='[' or ch =='{':
                stack.append(ch)
            else:
                if not stack:
                    return False 
                elif ch == ')' and stack[-1] == '(':
                    stack.pop()
                elif ch == ']' and stack[-1] == '[':
                    stack.pop()
                elif ch == '}' and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
                    
                