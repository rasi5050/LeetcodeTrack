"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # print(node.neighbors[0].neighbors)
        
        """ coudnt complete; mental block in deciding how reverse mapping works; ie. if a->b then how should i connect b->a, then stop at only b->a not looping infinitely
        #intuition do via BFS
        nodeClone1=nodeCloneTemp=Node(1)
        frontier=[node]
        while frontier:
            next=[]
            for nod in frontier:
                nodeCloneTemp=Node(nod.val)
                for neighbor in nod.neighbors:
                    nodeCloneTemp.neighbors.append(Node(neighbor.val))
            
                <do something>
            frontier=next
            
        """
        
        #help obtained from neetcode neetcode youtube solution to use hashmap and dfs
        hashMap={}
        def dfs(curNode):
            if curNode in hashMap: return hashMap[curNode]
            
            clone=Node(curNode.val)
            hashMap[curNode] = clone
            
            for neighbor in curNode.neighbors:
                clone.neighbors.append(dfs(neighbor))
            return clone
        return dfs(node) if node else None
            
            
            
            
            