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
                
        