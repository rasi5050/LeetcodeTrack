class TreeNode:
    def __init__(self):
        self.children={}
        self.word=False
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """wrong solution: attempted using tries; dont know to implement case
        #"aaaaaaa"
        #["aaaa","aaa"]
        root=node=TreeNode()
        lvl=0
        #insert word into prefix tree
        def insert(wordDict):
            nonlocal lvl
            nonlocal node
            for word in wordDict:
                for c in word:
                    if c in node.children:
                        node=node.children[c]
                    else:
                        new_node=TreeNode()
                        node.children[c]=new_node
                        node=new_node
                node.word=True
                node=root
        insert(wordDict)
    
        #search in prefix trie
        #if it was only leet, how would you do?
        def search(j):
            node=root
            for i in range(j, len(s)):
                if s[i] not in node.children:
                    return False
                node=node.children[s[i]]
                if node.word and i<len(s)-1:
                    print('hit@', i)
                    return search(i+1)
            return node.word
        return search(0)
        """
        # solution form neetcode youtube video (https://www.youtube.com/watch?v=Sx9NNgInc3A&t=5s)
        dp = [False] * (len(s)+1)        
        dp[len(s)] = True #base case
        for i in range(len(s) -1, -1, -1): #equivalent to last element to first element
            for w in wordDict:
                if (i+len(w)) <= len(s) and s[i: i + len(w)] == w:
                    dp[i]=dp[i + len(w)]
                if dp[i]:
                    break
        return dp[0]
                        
    
        