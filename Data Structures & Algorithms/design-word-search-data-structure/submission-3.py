class Node:
    def __init__(self):
        self.children = defaultdict(Node)
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            curr = curr.children[c]
        curr.is_word = True
    
    def dfs(self, word, root):
        curr = root
        for i, c in enumerate(word):
            if c == '.':
                for child in curr.children.values():
                    if self.dfs(word[i+1:], child):
                        return True
                return False
            else:
                if c not in curr.children:
                    return False
                curr = curr.children[c]
        return curr.is_word

    def search(self, word: str) -> bool:
        return self.dfs(word, self.root)

