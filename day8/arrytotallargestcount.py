arr = [2, 2, 1, 1, 1, 2, 2]

mp = {}

# Step 1: Array ko hash map (frequency) me convert karo
for n in arr:
    mp[n] = mp.get(n, 0) + 1

# Step 2: Maximum count nikaalo
m = max(mp.values())

print(m)
