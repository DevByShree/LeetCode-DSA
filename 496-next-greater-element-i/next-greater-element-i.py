class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        mp = {}
        res = []
        for i in range(len(nums2)):

            while stack and nums2[i] > stack[-1]:
                mp[stack[-1]] = nums2[i]
                stack.pop()
            stack.append(nums2[i])
        
        while stack:
            mp[stack[-1]] = -1
            stack.pop()
        
        for i in nums1:
            res.append(mp[i])
        return res



                    



                    


                        
                    
