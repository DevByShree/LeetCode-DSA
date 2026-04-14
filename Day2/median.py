# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

# Input: nums1 = [1,3], nums2 = [2]




# median = 1+3/2
# print("num1:",median)
# print("num2:",nums2)
# class Solution:
      
#     def med(self,nums1):
#         median = (nums1[0]+nums1[1])/2
#         return median       
# nums1 = [1,3]
# obj = Solution()
# n = obj.med(nums1)
# print(n)
      
      

class Solution:
      num1 = [1,3]
      num2 = [2]

      def findMeridianSortedArrays(self,num1,num2):
        arr = num1+num2
        arr.sort()

        n = len(arr)

        if n % 2 ==1:
            return arr[n//2]
        else:
            return(arr[n//2 - 1] + arr[n//2]) / 2

            
