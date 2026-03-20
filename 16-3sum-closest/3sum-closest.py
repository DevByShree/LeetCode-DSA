class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        closest_sum = float('inf')

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                # Update closest sum
                if abs(target - total) < abs(target - closest_sum):
                    closest_sum = total

                # Move pointers
                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    return total  # exact match

        return closest_sum