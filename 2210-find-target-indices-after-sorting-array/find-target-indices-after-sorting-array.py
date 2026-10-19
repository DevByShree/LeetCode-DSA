class Solution(object):
    def targetIndices(self, nums, target):
        nums.sort()
        store = []

        for i in range(len(nums)):
            if nums[i] == target:
                store.append(i)
        return store
        