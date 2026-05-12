class Solution(object):
    def maxFrequencyElements(self, nums):
        hash_map={}

        for char in nums:
            if char not in hash_map:
                hash_map[char] =1
            else:
                hash_map[char] +=1
        max_val = max(hash_map.values())

        result = []

        for key,value in hash_map.items():
            if value == max_val:
                result.append(value)
        curr_sum = sum(result)
        return curr_sum