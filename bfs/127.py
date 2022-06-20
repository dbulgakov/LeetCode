from collections import deque, defaultdict


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):

        graph = defaultdict(list)
        for word in wordList:
            for index in range(len(beginWord)):
                graph[word[:index] + "_" + word[index + 1:]].append(word)

        queue = deque()
        queue.append((beginWord, 1))
        visited = set()
        while queue:
            current_node, current_level = queue.popleft()
            if current_node == endWord:
                return current_level

            for index in range(len(beginWord)):
                node = current_node[:index] + "_" + current_node[index + 1:]
                for neighbour in graph[node]:
                    if neighbour not in visited:
                        queue.append((neighbour, current_level + 1))
                        visited.add(neighbour)
                graph[node] = []

        return 0