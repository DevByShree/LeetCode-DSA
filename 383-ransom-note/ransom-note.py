class Solution(object):
    def canConstruct(self, ransomNote, magazine):

        ransom_map = {}
        magazine_map = {}

        # ransomNote count
        for char in ransomNote:
            if char not in ransom_map:
                ransom_map[char] = 1
            else:
                ransom_map[char] += 1

        # magazine count
        for char in magazine:
            if char not in magazine_map:
                magazine_map[char] = 1
            else:
                magazine_map[char] += 1

        # compare
        for char in ransom_map:

            if char not in magazine_map:
                return False

            if ransom_map[char] > magazine_map[char]:
                return False

        return True