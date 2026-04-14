nums = [1,3,5,6]
target = 7
found = False
for i in range(len(nums)):
    if target == nums[i]:
        print(target)
        found:True
        break
if not found:   
    nums.append(target)
    nums.sort()
    print(nums)   