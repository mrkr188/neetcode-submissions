class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0

        adj = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                adj[pattern].append(word)

        queue = deque([beginWord])
        visited = set(beginWord)
        res = 1
        while queue:
            for i in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return res
                for i in range(len(word)):
                    pattern = word[:i] + '*' + word[i+1:]
                    print(word, adj[pattern], queue)
                    for nei in adj[pattern]:
                        # word will be present in the pattern
                        # we dont need to add it again to queue to bfs from there
                        if nei != word:
                            queue.append(nei)
                    # make pattern empty, no reason to search this path again
                    adj[pattern] = []
            res += 1
        return 0 


