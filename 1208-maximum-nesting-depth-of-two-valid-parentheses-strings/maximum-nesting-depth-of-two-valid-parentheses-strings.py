class Solution(object):
    def maxDepthAfterSplit(self, seq):
        depth = 0
        answer =[]

        for i in seq:
            if i =="(":
                depth +=1
                answer.append((depth+1)%2)
            else:
                answer.append((depth+1)%2)
                depth -=1
        return answer