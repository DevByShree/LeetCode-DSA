nums = [3,4,5,6]
target = 7

mp ={}

for i in range(len(nums)):
    bag = target - nums[i]
    if bag in mp:
        print(bag,nums[i])
    mp[nums[i]] = i