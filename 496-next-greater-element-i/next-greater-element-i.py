class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        store = []

        for i in range(len(nums1)):
            found = False
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    for k in range(j+1,len(nums2)):
                        if nums2[k]>nums1[i]:
                            store.append(nums2[k])
                            found = True
                            break
                    if found == False:
                        store.append(-1)
        return store 
                    


                        
                    
