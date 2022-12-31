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
        #status: correct, 2nd try didnt come up with solution; solution from neetcode youtube solution(https://www.youtube.com/watch?v=Sx9NNgInc3A&t=689s)
        #ref: 12/31/2022P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day68/68,1.wordBreakProblemTimed25Mins-x1pomo(5:30-6:00),2.implement-x2pomo(6:00-7:00),3.combinationSumTimed25Mins-x1pomo(7:00-7:30),4.implement-x2pomo(7:30-8:30),5.houseRobber2Timed25Mins-x1pomo(8:30-9:00),6.implement-x2pomo(9:00-10:00),7.decodeWaysTimed25Mins-x1pomo(10:00-10:30),8.implement-x2pomo(10:30-11:30)=x12pomo(5:30-11:30)delayed(6:30-11:30)1.wordBreakProblemTimed25Mins-x1pomo(6:30-7:00),2.implement-x2pomo(7:00-8:00),3.combinationSumTimed25Mins-x1pomo(8:00-8:30),4.implement-x2pomo(8:30-9:30),5.houseRobber2Timed25Mins-x1pomo(9:30-10:00),6.implement-x2pomo(10:00-11:00),7.decodeWaysTimed25Mins-x1pomo(11:00-11:30)

        