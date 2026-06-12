class Solution(object):
    def isPalindrome(self, s):

        clean = ""
        for ch in s:

            if ch.isalnum():
                clean += ch.lower()
        
        if clean == clean[::-1]:
            return True

        return False



