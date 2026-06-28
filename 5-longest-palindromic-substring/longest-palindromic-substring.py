class Solution(object):
    def longestPalindrome(self, s):
        result =""
        ans =""
        for i in range(len(s)):
            for j in range(i,len(s)):
                result = s[i:j+1]
                if result == result[::-1] and len(result)>len(ans):
                    ans = result 
        return ans 
