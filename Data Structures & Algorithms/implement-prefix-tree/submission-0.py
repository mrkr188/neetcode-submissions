class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            curr = curr.children[c]
        curr.is_word = True     

    def search(self, word: str) -> bool:
        curr = self.root
        for letter in word:
            curr = curr.children.get(letter)
            if curr is None:
                return False
        return curr.is_word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for letter in prefix:
            curr = curr.children.get(letter)
            if curr is None:
                return False
        return True
        
        