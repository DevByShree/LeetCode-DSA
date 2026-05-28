class Solution(object):
    def sortArrayByParity(self, nums):
        store = []
        for i in range(len(nums)):
            if nums[i] %2 == 0:
                store.append(nums[i])
        for i in range(len(nums)):
            if nums[i] %2 != 0:
                store.append(nums[i])
        return store
