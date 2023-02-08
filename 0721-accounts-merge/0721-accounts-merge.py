class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph=defaultdict(list)
        
        for account in accounts:
            for i in range(2, len(account)):
                graph[account[i]].append(account[i-1])
                graph[account[i-1]].append(account[i])
        visited=set()
        def dfs(email):
            visited.add(email)
            res=[email]
            # print(id(res), res)
            for connectedEmail in graph[email]:
                if connectedEmail not in visited:
                    res.extend(dfs(connectedEmail))
                    # print(id(res), res)
            return res
        ans=[]     # this would be returned as a list of list
        for account in accounts:
            if account[1] not in visited:
                ans.append([account[0]] + sorted(dfs(account[1])))
        return ans
        """
        #synopsis: emails are connected as a to b, so that connected components will be identified as to a single person and a dfs() on any of his emails will lead to all other emails that he owns. 
        graph is represented as {a:b
                                b:c
                                c:a}
        
        for each first email of a person , we do a dfs, esesntially retrieving his entire connected emails, visited list prevents from duplicating
        """
        #status: correct; help(https://leetcode.com/problems/accounts-merge/discuss/1601960/C%2B%2BPython-Simple-Solution-w-Images-and-Explanation-or-Building-Graph-and-DFS)
        #Analysis: Time O(NML*log(MN)), help(https://leetcode.com/problems/accounts-merge/discuss/1601960/C%2B%2BPython-Simple-Solution-w-Images-and-Explanation-or-Building-Graph-and-DFS)
        #ref: 2/8/2023P2:track1-cpGrind75;Day104/104;doLeetcodeBlind75-3q/day-17/45Q:completeOn2/15/2023-Day12/15,collateQuestionPatternIntoCategoriesAndTemplaye-Day3/3:(addWordDescriptionOnceProblemIsSolvedDay2/2)1.(accountsMergeTimed25Mins)-x1pomo(6:00-6:30),2.implement(addDescriptionAfterSolvingProblem)-x1pomo(6:30-7:00),3.sortColorsTimed25Mins-x1pomo(7:00-7:30),4.implement(addDescriptionAfterSolvingProblem)-x1pomo(7:30-8:00),5.absorber-x2pomo(8:00-9:00),6.wordBreakTimed25Mins-x1pomo(9:00-9:30),7.implement-x1pomo(9:30-10:00),8.applyInternships(1.https://www.tesla.com/careers/search/job/software-data-platforms-engineering-internship-summer-2023-153313?source=LinkedIn,2.https://www.applicantpro.com/openings/netcentrics/jobs/2753633-478257,3.https://careers.intuitive.com/us/en/job/JOB2747/DevOps-Intern?utm_source=linkedin&utm_medium=phenom-feeds,4.https://boards.greenhouse.io/schonfeld/jobs/4839329?gh_src=e73f47fb1us,5.https://jobs.lever.co/milhouseinc/923fc470-3ddf-4d35-87b2-2699657fcfcb,6.https://jobs.keysight.com/job/Loveland-R&D-DevOps-Internship-CO-80534/980654100/?feedId=217500&utm_source=LILimitedListings&utm_campaign=Keysight_LinkedinLL)-x2pomo(10:00-11:00)-x12pomo(5:30-11:30)alter-x10pomo(6:00-11:00)