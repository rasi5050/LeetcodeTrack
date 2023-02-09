class Trie:
    def __init__(self):
        self.children={}
        self.isWord=False
    
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """solution from (https://leetcode.com/problems/word-break/discuss/1455100/Python-3-solutions%3A-Top-down-DP-Bottom-up-DP-then-Optimised-with-Trie-Clean-and-Concise)
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
    """
        lenS=len(s)
        #alter solution
        dp=[False]*(lenS+1)
        dp[lenS]=True
        
        for i in range(lenS-1, -1, -1):
            for w in wordDict:
                if i+len(w)<=lenS and s[i:i+len(w)]==w:
                    dp[i]=dp[i+len(w)]
                if dp[i]:
                    break
        return dp[0]
    #status: correct; didnot understand ; help(https://www.youtube.com/watch?v=Sx9NNgInc3A&t=929s)
    #Analysis: Time O(n^2), Space O(n)
    #ref:2/9/2023P2:track1-cpGrind75;Day105/106;doLeetcodeBlind75-3q/day-18/45Q:completeOn2/15/2023-Day13/15,collateQuestionPatternIntoCategoriesAndTemplate-Day4/5:(addWordDescriptionOnceProblemIsSolvedDay3/4),1.sortColorsTimed25Mins-x1pomo(6:00-6:30),2.implement(addDescriptionAfterSolvingProblem)-x1pomo(6:30-7:00),3.wordBreakTimed25Mins-x1pomo(7:00-7:30),4.implement-x1pomo(7:30-8:00),5.partitionEqualSubsetSumTimed25Mins-x1pomo(8:00-8:30),6.implement-x1pomo(8:30-9:00),7.absorber-x2pomo(9:00-10:00),8.applyInternships(0.(P2:searchInternshipInTiktokWebsite(https://careers.tiktok.com/position/7138620933615733006/detail);1.Please state your availability clearly in your resume (Start date, End date).(1. May 22, 2023 to August 11, 2023),2.applyOtherPositionIfAllowed,3.addDockerExperienceToResume)
#,1.https://www.adzuna.com/details/3913091385?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic,2.https://allengerritsen.applytojob.com/apply/v9MoFr2gnx/Summer-2023-DevOps-Intern?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic,3.https://adelatech.com/adelatech-jobs/cloud-architect-and-devops-intern-apprentice/?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic,4.https://www.monster.com/job-openings/software-engineer-devops-summer-internship-weston-ma--9526b6fa-3381-4622-9d6f-5d023867f090?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic,5.https://www.ziprecruiter.com/c/Bose-Corporation/Job/Security-DevOps-Engineering-Intern/-in-Framingham,MA?jid=a053022317016772&utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic,6.https://ct.tarta.ai/j/14FJ14QBvf0LOA5Ejt3O1222-devops-engineer-intern-in-danbury-connecticut-at-experian?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic)-x2pomo(10:00-11:00)-x12pomo(5:30-11:30)alter-x10pomo(6:00-11:00)
