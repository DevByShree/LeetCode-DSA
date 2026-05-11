class Solution(object):
    def findTheDifference(self, s, t):
        hash_map={}

        for char in s:
            if char not in hash_map:
                hash_map[char] = 1
            else:
                hash_map[char]+=1
        for char in t :
            if char not in hash_map:
                hash_map[char]=1
            else:
                hash_map[char]-=1
        for char in hash_map:
            if hash_map[char] !=0:
                return char
