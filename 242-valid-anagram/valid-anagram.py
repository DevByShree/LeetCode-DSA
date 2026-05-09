class Solution(object):
    def isAnagram(self, s, t):
        hash_map={}
        for char in s:
            if char in hash_map:
                hash_map[char] +=1
            else:
                hash_map[char] = 1
        
        for char in t:
            if char not in hash_map:
                return False
            
            hash_map[char] -= 1

        for  value in hash_map.values():
            if value!=0:
                return False
        return True
