class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # build the Trie from the list of words
        root = {}
        for word in words:
            curr = root
            for char in word:
                if char not in curr:
                    curr[char] = {}
                curr = curr[char]
            curr['#'] = word  # store the complete word at the terminal node
            
        rows, cols = len(board), len(board[0])
        res = set()
        
        def dfs(r, c, curr):
            char = board[r][c]
            if char not in curr:
                return
            
            next_node = curr[char]
            # if we hit a complete word, add it to our results set
            if '#' in next_node:
                res.add(next_node['#'])
                # optionally, we can delete '#' here to avoid duplicate additions if needed,
                # but a result set handles duplicates cleanly.
                
            # temporarily mark the current cell as visited
            board[r][c] = '#'
            
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != '#':
                    dfs(nr, nc, next_node)
                    
            # restore the cell value after backtracking
            board[r][c] = char
            
        # initiate DFS from every cell on the board
        for r in range(rows):
            for c in range(cols):
                if board[r][c] in root:
                    dfs(r, c, root)
                    
        return list(res)


# class TrieNode():
#     def __init__(self):
#         self.children = collections.defaultdict(TrieNode)
#         self.isWord = False
    
# class Trie():
#     def __init__(self):
#         self.root = TrieNode()
    
#     def insert(self, word):
#         node = self.root
#         for c in word:
#             node = node.children[c]
#         node.isWord = True
    
#     def search(self, word):
#         node = self.root
#         for c in word:
#             node = node.children.get(c)
#             if not node:
#                 return False
#         return node.isWord

# class Solution:
#     def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
#         res = []
#         trie = Trie()
#         node = trie.root
#         for w in words:
#             trie.insert(w)
#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 self.dfs(board, node, i, j, "", res)
#         return res
    
#     def dfs(self, board, node, i, j, path, res):
#         if node.isWord:
#             res.append(path)
#             node.isWord = False
            
#         if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
#             return 
#         tmp = board[i][j]
#         node = node.children.get(tmp)
#         if not node:
#             return 
#         board[i][j] = "#"
#         for x, y in [(i-1, j), (i, j-1), (i, j+1), (i+1, j)]:
#             self.dfs(board, node, x, y, path+tmp, res)
#         board[i][j] = tmp


