# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
# Example 1:
nums = [1,2,3,1]

mp = {}

for n in nums:
    mp[n] = mp.get(n,0)+1
    m = max(mp , key=mp.get)
    if m>1:
        print("false")
    else:
        print("True")   
    break 
