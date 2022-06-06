class Trie:
    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        node = self.trie

        for letter in word:
            if letter not in node:
                node[letter] = {}
            node = node[letter]

        node['end'] = True

    def search(self, word: str) -> bool:
        node = self.trie

        for letter in word:
            if letter in node:
                node = node[letter]
            else:
                return False

        return 'end' in node

    def startsWith(self, prefix: str) -> bool:
        node = self.trie

        for letter in prefix:
            if letter in node:
                node = node[letter]
            else:
                return False

        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)