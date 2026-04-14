strs = ["act","pots","tops","cat","stop","hat"]

sorted_words = []
for word in strs:
    sorted_words.append(''.join(sorted(word)))

main = []

for i in range(len(sorted_words)):
    group = [strs[i]]
    for j in range(i+1, len(sorted_words)):
        if sorted_words[i] == sorted_words[j]:
            group.append(strs[j])

    main.append(group)

print(main)