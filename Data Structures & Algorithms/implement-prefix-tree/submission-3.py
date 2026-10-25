class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False

class PrefixTree:
    """
    Root (TrieNode)
    └── 'c' (children['c'])
        └── 'a' (children['a'])
            ├── 't' (children['t'], is_word = True)  <-- "cat" ends here
            └── 'r' (children['r'], is_word = True)  <-- "car" ends here
    """
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



  