class Solution(object):
    def calPoints(self, operations):
        stack = []

        for current in operations:
            if  current =='C':
                stack.pop()

            elif current == 'D':
                stack.append(stack[-1]*2)

            elif stack and  current =="+":
                stack.append(stack[-1]+stack[-2])
            else:
                stack.append(int(current))
        return sum(stack)


