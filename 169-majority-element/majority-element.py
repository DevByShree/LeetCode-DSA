class Solution(object):
    def majorityElement(self, nums):
        mp ={}

        for i in nums:
            if i not in mp:
                mp[i] = 1
            else:
                mp[i] +=1 
        return max(mp,key=mp.get)