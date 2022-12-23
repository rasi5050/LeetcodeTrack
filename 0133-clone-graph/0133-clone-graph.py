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
    #status: correct (complete help from neetcode youtube solution ((https://www.youtube.com/watch?v=mQeF6bN8hMk&t=707s)))
    #analysis: Time O(|V|+|E|); visiting all nodes once, 
    #Space O(|V| + |E|); entire graph is clone and stored
    #ref: 12/23/2022P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day59/60,1.cloneGraphTimed25Mins-x1pomo(5:30-6:00),2.implement-x2pomo(6:00-7:00),3.pacificAtlanticWaterFlowTimed25Mins-x1pomo(7:00-7:30),4.implement-x2pomo(7:30-8:30),5.courseScheduleTimed25Mins-x1pomo(8:30-9:00),6.implement-x2pomo(9:00-10:00),7.studyHeap-x1pomo(10:00-10:30),8.mergeKSortedListsTimed25Mins-x1pomo(10:30-11:00),9.implement-x1pomo(11:00-11:30)=x12pomo(5:30-11:30)

    
            
            
            
            
            