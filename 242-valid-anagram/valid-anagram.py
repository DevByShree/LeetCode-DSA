class Solution(object):
    def isAnagram(self, s, t):
        mp = {}

        for key in s:
            if key not in mp:
                mp[key] = 1
            else:
                mp[key] +=1

        for key in t:
            if key not in mp:
                return False 
            else:
                mp[key] -=1
        for value in mp.values():
            if value!=0:
                return False
        return True 

