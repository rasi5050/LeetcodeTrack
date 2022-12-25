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

#status: correct; help from comments to leetcode article on trie of user:"inawhsa" (Feb 28, 2021); (https://leetcode.com/problems/implement-trie-prefix-tree/solutions/127843/official-solution/)
#Analysis: Time; insert O(m), where m is the word length, search O(m), search_prefix O(m)
#Space; insert O(m); word might not be present, search O(1); no space requirement for search, search_prefix O(1); no space requirement for search_prefix
#ref: 12/25/2022P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day61/62,1.studyTrie-x1pomo(5:30-6:00),2.implementTrieTimed25Mins-x1pomo(6:00-6:30),3.implement-x2pomo(6:30-7:30),4.addAndSearchWorkdTimed25Mins-x1pomo(7:30-8:00),5.implement-x2pomo(8:00-9:00),6.wordBreakTimed25Mins-x1pomo(9:00-9:30),7.implement-x2pomo(9:30-10:30),8.wordSearch2Timed25Mins-x1pomo(10:30-11:00),9.implement-x1pomo(11:00-11:30)=x12pomo(5:30-11:30)
