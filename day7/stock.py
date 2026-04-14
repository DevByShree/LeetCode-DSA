prices = [7,1,5,3,6,4]
m=min(prices)

for i in range(n-1,min,1):
    sum = prices[i]
    k = sum - m

k.sort()
print(max(k))

