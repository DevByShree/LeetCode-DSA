class Solution(object):
    def rearrangeArray(self, nums):
        positive = []
        negative = []
        result =[]

        for i in nums:
            if i > 0:
                positive.append(i)
            elif i < 0:
                negative.append(i)
        for i in range(len(positive)):
            result.append(positive[i])
            result.append(negative[i])
        return result 
        