class Solution:
    def suggestedProducts(self, products: list[str], searchWord: str) -> list[list[str]]:
        products.sort()
        t = Trie()
        for product in products:
            t.insert(product)

        res = []
        word = ''
        for char in searchWord:
            word += char
            res.append(t.search(word))

        return res


class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word: str):
        current = self.root
        for char in word:
            if char not in current:
                current[char] = {}
            current = current[char]
        current['end'] = True

    def search(self, word: str):
        current = self.root
        for char in word:
            if char not in current:
                return []
            current = current[char]
        self.result = []
        self.dfs(current, word)
        return self.result[:3]

    def dfs(self, node, word: str):
        for value in node:
            if value == 'end':
                self.result.append(word)
            else:
                self.dfs(node[value], word + value)
