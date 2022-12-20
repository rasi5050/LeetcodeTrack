# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []        
        def dfs(node):
            if not node: 
                res.append('N')
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res)

    def deserialize(self, data):
        
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(',')
        self.i = 0
        
        def dfs():
            if vals[self.i] == 'N':
                self.i+=1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i+=1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


#status: correct: complete help from neetcode youtube solution(https://www.youtube.com/watch?v=u4JAi2JJhI8)
#analysis: Time O(n); preorder traversal, Space O(n); if serialized array is considered
#ref: 12/20/2022P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day56/56,1.constructBinaryTreeFromPreorderAndInorderTraversalTimed25Mins-x1pomo(5:30-6:00),2.implement-x2pomo(6:00-7:00),3.serializeAndDeserializeBinaryTreeTimed25Mins-x1pomo(7:00-7:30),4.implement-x2pomo(7:30-8:30),5.validateBinarySearchTreeTimed25Mins-x1pomo(8:30-9:00),6.implement-x2pomo(9:00-10:00),7.kThSmallestElementInABstTimed25Mins-x1pomo(10:00-10:30),8.implement-x2pomo(10:30-11:30)=x12pomo(5:30-11:30)
