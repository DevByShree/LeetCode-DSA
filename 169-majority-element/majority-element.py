class Solution(object):
    def majorityElement(self, nums):
        hash_map={}
        for num in nums:
            if num in hash_map:
                hash_map[num] +=1
            else:
                hash_map[num] = 1
        for key,value in hash_map.items():
            if value > len(nums)//2:
                return key