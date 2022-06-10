from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}

        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            min_len = min(len(word1), len(word2))

            if len(word1) > len(word2) and word1[:min_len] == word2[:min_len]:
                return ''

            for j in range(min_len):
                if word1[j] != word2[j]:
                    adj[word1[j]].add(word2[j])
                    break

        seen = {}
        res = []

        def dfs(c: str) -> bool:
            if c in seen:
                return seen[c]

            seen[c] = True
            for nei in adj[c]:
                if dfs(nei):
                    return True

            seen[c] = False
            res.append(c)

        for c in adj:
            if dfs(c):
                return ''

        return ''.join(reversed(res))


