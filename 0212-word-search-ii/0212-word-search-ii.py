class TrieNode:
    def __init__(self):
        self.children={}
        self.isWord=False
    def addWord(self, word):
        node=self
        #add the words to check to trie
        for c in word:
            if c not in node.children:
                node.children[c]=TrieNode()
            node=node.children[c]
        node.isWord=True
        
    def prune(self, word): #added new
        curr = self
        stack = []        
        for ch in word:
            stack.append(curr)
            curr = curr.children[ch]
        curr.is_word = False
        for t_node, ch in reversed(list(zip(stack, word))):
            if len(t_node.children[ch].children) > 0:  # has children
                return
            else:
                del t_node.children[ch]
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root=TrieNode()
        for w in words:
            root.addWord(w)
        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()
        
        def dfs(r, c, node, word):
            if (r<0 or c<0 or
               r==ROWS or c==COLS or
               board[r][c] not in node.children or (r,c) in visit):
                return
            visit.add((r, c))
            node=node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)
                root.prune(word)  #added new
                
            dfs(r+1, c, node, word)
            dfs(r-1, c, node, word)
            dfs(r, c-1, node, word)
            dfs(r, c+1, node, word)
            visit.remove((r, c))  #didnot understand this line
            
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
        return list(res)
    #status: correct(complete help from ne)
                