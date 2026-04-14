nums = [0,1,0,3,12] 

i = 0
while i < len(nums):
    if nums[i] == 0:
        nums.pop(i)     # zero hatao
        nums.append(0)  # last me daalo
    else:
        i += 1

print(nums)
