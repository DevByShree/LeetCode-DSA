class Solution(object):
    def findContentChildren(self, g, s):
        # Step 1: Sort both arrays
        g.sort()
        s.sort()
        
        i = 0  # child pointer
        j = 0  # cookie pointer
        
        count = 0
        
        # Step 2: Assign cookies
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                count += 1
                i += 1
                j += 1
            else:
                j += 1
        
        return count