s = "racecar"
t = "carrace"

if len(s) != len(t):
    print(False)
elif sorted(s) == sorted(t):
    print(True)
else:
    print(False)
