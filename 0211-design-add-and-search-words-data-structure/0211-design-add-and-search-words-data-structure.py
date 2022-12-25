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
        #status: correct; blind copy from neetcode youtube solution (https://www.youtube.com/watch?v=BTf05gs_8iU&t=1163s)
        #improvements in video comments: user "Lulit999" comments to video; he also given it in leetcode comments (https://leetcode.com/problems/design-add-and-search-words-data-structure/discuss/2622355/Do-you-have-TLE-Add-this-one-thing-to-your-code!) 
        #Analysis: Time O(m*n); for a word all the tree might have to be recursed
        #Space O(m*n); n words of size m stored
        #ref: 12/25/2022P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day61/62,1.studyTrie-x1pomo(5:30-6:00),2.implementTrieTimed25Mins-x1pomo(6:00-6:30),3.implement-x2pomo(6:30-7:30),4.addAndSearchWorkdTimed25Mins-x1pomo(7:30-8:00),5.implement-x2pomo(8:00-9:00),6.wordBreakTimed25Mins-x1pomo(9:00-9:30),7.implement-x2pomo(9:30-10:30),8.wordSearch2Timed25Mins-x1pomo(10:30-11:00),9.implement-x1pomo(11:00-11:30)=x12pomo(5:30-11:30)
