class Solution:
    def twoSum(self, nums, target):
        bag = {}

        for i in range(len(nums)):
            need = target - nums[i]
            if need in bag:
                return [bag[need], i]
            bag[nums[i]] = i
