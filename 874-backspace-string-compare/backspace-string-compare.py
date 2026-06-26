class Solution(object):
    def backspaceCompare(self, s, t):
        stack1 = []
        stack2 = []

        for current in s:
            if current == "#":
                if stack1:
                    stack1.pop()
            else:
                stack1.append(current)
        for key in t:
            if key =="#":
                if stack2:
                    stack2.pop()
            else:
                stack2.append(key)
        return stack1==stack2



        