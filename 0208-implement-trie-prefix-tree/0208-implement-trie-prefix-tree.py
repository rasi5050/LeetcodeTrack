class Node:
    def __init__(self):
        self.children={}
        self.isWord=False

class Trie:

    def __init__(self):
        self.root=Node()

    def insert(self, word: str) -> None:
        node=self.root
        for c in word:
            if c in node.children:
                node=node.children[c]
            else:
                new_node=Node()
                node.children[c]=new_node
                node=node.children[c]
            # print(node)
        node.isWord=True

    def search(self, word: str) -> bool:
        node=self.root
        for c in word:
            if c in node.children:
                node=node.children[c]
            else:
                return False
        return node.isWord

    def startsWith(self, prefix: str) -> bool:
        node=self.root
        for p in prefix:
            if p in node.children:
                node=node.children[p]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)