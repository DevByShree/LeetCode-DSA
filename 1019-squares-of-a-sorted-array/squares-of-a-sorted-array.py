class Solution(object):
    def sortedSquares(self, nums):
        stores =[]
        for num in nums:
            stores.append(num**2)
            stores.sort()
        return stores