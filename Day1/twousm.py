# TWO SUM PYTHON 
#  brute force 
# nums = [2,7,11,15]
# target = 9 

# for i in range (len(nums)):
#     for j in range (i+1,len(nums)):
#         if nums[i] + nums [j] == target:
#             print(i,j)


nums = [2,7,11,15]
target = 9 

class Solution:
    deftwosum(nums,target):
    bag={} 
    for i in range(len(nums)):
        need =  target - nums[i]

        if need in bag:
            return bag[[need],i]

        bag[nums[i]] = i