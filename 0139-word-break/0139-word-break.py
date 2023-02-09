class Trie:
    def __init__(self):
        self.children={}
        self.isWord=False
    
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        root=curr=Trie()
        def addWordToTrie(word):
            node=root
            for char in word:
                if char in node.children:
                    node=node.children[char]
                else:
                    new_node=Trie()
                    node.children[char]=new_node
                    node=node.children[char]
            node.isWord=True
        
        #add words to trie
        for word in set(wordDict):
            addWordToTrie(word)
        lenS=len(s)
        dp=[False]*(lenS+1)       #considered as, string s[i:]  is possible if string s[i+1:] is possible, where the base condition is empty string is possible 
        dp[lenS]=True
        #take index in reverse order
        for i in range(lenS-1,-1,-1):
            #check the string s[lenS-1+1:] is present in trie
            node=root
            
            for j in range(i+1, lenS+1):  #lenS+1 since it will go till lenS
                c=s[j-1]
                if c not in node.children: break
                node=node.children[c]
                if node.isWord and dp[j]:
                    dp[i]=True
                    break
        return dp[0]