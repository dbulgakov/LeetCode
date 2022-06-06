class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        node = self.trie

        for letter in word:
            if letter not in node:
                node[letter] = {}
            node = node[letter]

        node['end'] = True

    def search(self, word: str) -> bool:
        def search_node(node: dict[str, dict], word: str) -> bool:
            for index, letter in enumerate(word):
                if letter in node:
                    node = node[letter]
                else:
                    if letter == '.':
                        for key in node.keys():
                            if key != 'end' and search_node(node[key], word[index + 1:]):
                                return True

                    return False

            return 'end' in node

        return search_node(self.trie, word)
