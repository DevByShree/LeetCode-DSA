class Solution(object):
    def firstStableIndex(self, nums, k):
        n = len(nums)

        for i in range(n):
            left_max = max(nums[0:i + 1])
            right_min = min(nums[i:n])

            instability = left_max - right_min

            if instability <= k:
                return i

        return -1