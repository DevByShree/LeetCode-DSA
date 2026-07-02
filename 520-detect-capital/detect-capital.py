class Solution(object):
    def detectCapitalUse(self, word):

        if word == word.upper():
            return True
        elif word == word.lower():
            return True
        elif word[0].isupper() and word[1:] == word[1:].lower():
            return True
        else:
            return False

        