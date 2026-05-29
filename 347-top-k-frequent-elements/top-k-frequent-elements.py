class Solution(object):
    def topKFrequent(self, nums, k):
        map = {}        
        for num in nums:
            if num in map:
                map[num] +=1
            else:
                map[num] = 1
        sorted_items = sorted(map.items(),key =lambda x:x[1],reverse=True)

        result =[]
        for i in range(k):
            result.append(sorted_items[i][0])
        return result

