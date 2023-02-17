class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #normal approach
        """
        @cache
        def dfs(i,j):
            if i>=m or j>=n:
                return 0
            if i==m-1 and j==n-1:
                return 1
            count=0
            count+=dfs(i+1,j)
            count+=dfs(i,j+1)
            return count
        return dfs(0,0)
        """
        """
        #alternate from bottom to top
        @cache
        def dfs(i,j):
            if i<0 or j<0:
                return 0
            if i==0 and j==0:
                return 1
            count=0
            count+=dfs(i-1,j)
            count+=dfs(i,j-1)
            return count
        return dfs(m-1,n-1)
        """
        #second approach is faster because less pruning of trees
    
        #status: correct
        #Analysis: Time O(2^(max(m,n))), Space O(2^(max(m,n)))
        #ref: 2/17/2023P2:track1-cpGrind75;Day111/112;doLeetcodeBlind75-3q/day-26/45Q:completeOn2/15/2023-Day19/15,collateQuestionPatternIntoCategoriesAndTemplate-Day9/5:(addWordDescriptionOnceProblemIsSolvedDay6/4),1.uniquePathsTimed25Mins-x1pomo(6:00-6:30),2.implement-x1pomo(6:30-7:00),3.constructABinaryTreeFromPreorderAndInorderTraversalTimed25Mins-x1pomo(7:00-7:30),4.implement-x2pomo(7:30-8:30),5.containerWithMostWaterTimed25Mins-x1pomo(8:30-9:00),6.implement-x1pomo(9:00-9:30),7.applyInternship-x6SdeFromGitHubPage-x2pomo(9:30-10:30),8.applyInternship-x3DevOpsFromLinkedIn-x1pomo(10:30-11:00)             -x12pomo(5:30-11:30)alter-x10pomo(6:00-11:00)

        #dp approach
        #number of paths depends of the smaller grid
        
        dp=[[0]*(n) for _ in range(m)]
        dp[0][0]=0.5
        for i in range(m):
            for j in range(n):
                dp[i][j]=dp[i-1 if (i-1)>=0 else i][j]+dp[i][j-1 if (j-1)>=0 else j]
        print(dp)
        return int(dp[m-1][n-1])
        