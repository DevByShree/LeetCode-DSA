class Solution(object):
    def groupAnagrams(self, strs):
        hash_map ={}

        for word in strs:
            key ="".join(sorted(word))

            if key not in hash_map:
                hash_map[key] = []

            hash_map[key].append(word)

        return hash_map.values()