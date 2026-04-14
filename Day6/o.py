nums = [3,2,2,3]
val = int(input(" Enter the vlaue"))
k = 0

for i in range(len(nums)):
    if nums[i] != val:
        nums[k]= nums[i]
        k+=1
print(k)
print(nums[:k])   
#  k means last value like k-1


# LEETCODE
# class Solution(object):
#     def removeElement(self, nums, val):
#         k = 0
#         for i in range(len(nums)):
#             if nums[i] != val:
#                 nums[k] = nums[i]
#                 k += 1
#         return k
