class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        res = ""
        for key in tokens:
            if key =="+":
                a = stack.pop()
                b = stack.pop()
                res = b + a
                stack.append(res)
            elif key =="-":
                a = stack.pop()
                b = stack.pop()
                res = b - a
                stack.append(res)
            elif key =="*":
                a = stack.pop()
                b = stack.pop()
                res = b * a
                stack.append(res)
            elif key =="/":
                a = stack.pop()
                b = stack.pop()
                res = int(float(b) / a)
                stack.append(res)
            else:
                stack.append(int(key))
        return stack.pop()