"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: 
            return None
        oldToNew={}
        def dfs(root):
            if root in oldToNew:
                return oldToNew[root]
            
            dummy=Node(root.val)
            oldToNew[root]=dummy
            for neig in root.neighbors:
                dummy.neighbors.append(dfs(neig))
                
            return dummy
        return dfs(node)