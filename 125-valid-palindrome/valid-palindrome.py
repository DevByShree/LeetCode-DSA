class Solution(object):
    def isPalindrome(self, s):
        clean =""

        for ch in s:
            if ch.isalnum():
                clean+= ch.lower()

        for i in range(len(clean)):
            j = len(clean)-1 -i
            if clean[i]!=clean[j]:
                return False
        return True