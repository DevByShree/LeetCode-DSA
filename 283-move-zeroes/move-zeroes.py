class Solution(object):
    def moveZeroes(self, nums):
        i = 0 
        zero = nums.count(0)

        while i < len(nums)-zero:
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
            else:
                i +=1
