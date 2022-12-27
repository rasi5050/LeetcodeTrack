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
        
    #below section not included in neetcode solution; added because neetcode solution resulted in TLE    
    def prune(self, word): #added new from neetcode comments user: @LeoK
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
    #section ends here
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
    #status: correct(complete help from neetcode solution(https://www.youtube.com/watch?v=asbcE9mZz_U)); didnot unserstand the implementation; which gave TLE, so added "def prune(self, word):" from neetcode comments by user: @LeoK
    #Analysis: Time O(mn*4^mn)
    #Space O(wordLength*numberOfWords)
    #ref: 12/27/2022P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day64/64,1.wordSearch2Timed25Mins-x1pomo(5:30-6:00),2.implement-x1pomo(6:00-7:00),3.studyIntervals-x1pomo(7:00-7:30),4.mergeIntervalsTimed;25Mins-x1pomo(7:30-8:00),5.implement-x2pomo(8:00-9:00),6.insertIntervalTImed25Mins-x1pomo(9:00-9:30),7.implement-x2pomo(9:30-10:30),8.nonOverlappingIntervalsTimed25Mins-x1pomo(10:30-11:00),9.absorber-x1pomo(11:00-11:30)=x12pomo(5:30-11:30)

                