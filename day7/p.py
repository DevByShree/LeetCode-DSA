nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]

m = 3 

n =nums1[:m]

n = n + nums2

n.sort()

for i in range(len(n)):
    nums1[i] =n[i]

print(nums1)    
