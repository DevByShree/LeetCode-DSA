class Solution(object):
    def thirdMax(self, nums):
        nums = list(set(nums))  # remove duplicates
        nums.sort()
        
        if len(nums) < 3:
            return nums[-1]
        else:
            return nums[-3]