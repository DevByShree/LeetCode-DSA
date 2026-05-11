class Solution(object):
    def longestPalindrome(self, s):

        hash_map = {}
    # hashing
        for char in s:
            if char not in hash_map:
                hash_map[char] = 1
            else:
                hash_map[char] += 1
        
        length = 0
        odd = False
        for value in hash_map.values():

            if value %2 ==0:
                length += value
            else:
                length += value-1
                odd =True

        if odd:
            length+=1
        return length

