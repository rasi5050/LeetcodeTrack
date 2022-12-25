"""wrong code: couldnt figure out error in search recursion
#implement using Trie
class TreeNode:
    def __init__(self, char=""):
        self.char=char
        self.children={}
        self.is_end=False
class WordDictionary:
    def __init__(self):
        self.root=TreeNode()

    def addWord(self, word: str) -> None:
        node=self.root
        for char in word:
            if char in node.children:
                node=node.children[char]
            else:
                node.children[char]=TreeNode(char)
                node=node.children[char]
        node.is_end=True
    
    
    def search(self, word: str, node=None) -> bool:
        node=node if node else self.root
        print(node)
        for char in word:
            if char == '.':
                for ch in node.children.values():
                    if search(word[1:], ch): return True    #couldnt figure out recursion
                print('result from recursion hit for word: ' + word)
                return False
            
            if char in node.children:
                node=node.children[char]
            else:
                return False
        return node.is_end
"""
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

class TreeNode:
    def __init__(self):
        self.children={}
        self.word=False
class WordDictionary:
    def __init__(self):
        self.root=TreeNode()

    def addWord(self, word: str) -> None:
        node=self.root
        for char in word:
            if char not in node.children:
                node.children[char]=TreeNode()
            node=node.children[char]
        node.word=True
    
    def search(self, word: str) -> bool:
        
        def dfs(j, root):
            cur=root
            for i in range(j, len(word)):
                c=word[i]
                if c == '.':
                    for child in cur.children.values():
                        if dfs(i+1, child): 
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur=cur.children[c]
            return cur.word
        return dfs(0, self.root)
        