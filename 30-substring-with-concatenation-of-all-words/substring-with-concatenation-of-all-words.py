class Solution(object):

    def findSubstring(self, s, words):

        if not s or not words:
            return []

        word_len = len(words[0])

        total_len = word_len * len(words)

        answer = []

        for i in range(len(s) - total_len + 1):

            substring = s[i:i + total_len]

            parts = []

            for j in range(0, total_len, word_len):

                parts.append(substring[j:j + word_len])

            if sorted(parts) == sorted(words):

                answer.append(i)

        return answer