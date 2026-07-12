class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        long_list = [] #[[1,2,3,4][5,6,7,8]]

        for i in matrix:
            long_list.extend(i)

        for j in long_list:
            if target == j:
                return True
        return False 


        