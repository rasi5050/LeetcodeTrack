"""
class TreeNode:
    def __init__(self):
        self.children={}
        self.isWord=False
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        #create Trie node for the list of words
        root=node=TreeNode()
        for word in wordDict:
            node=root
            for c in word:
                if c not in node.children:
                    new_node=TreeNode()
                    node.children[c]=new_node
                node=node.children[c]
            node.isWord=True
        """
        #i remember this question had edge case of 'aaa', 'aaaa', to be matched with 'aaaaaaa', linear searching will only create 'aaa' 2 times and hence fails to create 'a' of 7 times
        
        #correlated to one of the answers
        
        #better approach in neetcode solution:
        
        dp = [False] * (len(s)+1)
        dp[len(s)] = True
        
        for i in range(len(s)-1, -1, -1):
            for word in wordDict:
                if (i+len(word)) <= len(s) and s[i: i+len(word)]==word:
                    dp[i] = dp[i + len(word)]
                if dp[i]:
                    break
        return dp[0] 
        