nums = [1, 2, 3, 4]
# patter hashmap
mp = {}

for i in range(len(nums)):
    if nums[i] in mp:
        print("True")
        break
    else:
        mp[nums[i]] = 1
else:
    print("False")
