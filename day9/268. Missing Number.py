nums = [3,0,1]

n = len(nums)

expected_nums = n *(n+1) // 2 # 6 
actual_nums = sum(nums)  #4

sum = expected_nums - actual_nums
print(sum) 

