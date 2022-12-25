class TreeNode:
    def __init__(self, char=""):
        self.char=char
        self.children={}
        self.is_end=False
class Trie:
    def __init__(self):
        self.root=TreeNode()

    def insert(self, word: str) -> None:
        node=self.root
        #insert each char to the trie
        for char in word:
            if char in node.children:
                node=node.children[char]
            else:
                node.children[char]=TreeNode(char)
                node=node.children[char]
        node.is_end=True
            
    def search(self, word: str) -> bool:
        node=self.root
        for char in word:
            if char in node.children:
                node=node.children[char]
            else:
                return False
        if node.is_end==True:
            return True
        else:
            return False
            
        

    def startsWith(self, prefix: str) -> bool:
        node=self.root
        for char in prefix:
            if char in node.children:
                node=node.children[char]
            else:
                return False
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)