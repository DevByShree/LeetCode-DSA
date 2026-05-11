class Solution(object):
    def firstUniqChar(self, s):
        map = {}
        for char in s:
            if char not in map:
                map[char] = 1
            else:
                map[char]+=1
            
        for i in range(len(s)):
            if map[s[i]] ==1:
                return i
        return -1
