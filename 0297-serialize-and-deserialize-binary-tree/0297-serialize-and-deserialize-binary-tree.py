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
        
        def recurse(root):
            if not root: 
                return '_;'   
            return '' + str(root.val) + ';' + str(recurse(root.left)) + str(recurse(root.right))
        return recurse(root)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        print(data)
        i=0
        root=TreeNode()
        def recurse(data, root):
            nonlocal i 
            if data[i]=='_':
                i+=2
                return None
            else:
                num=''
                while (data[i].isdigit()) or data[i]=='-':
                    num+=data[i]
                    i+=1
                i+=1
                root=TreeNode(num)
                root.left=recurse(data, root.left)
                root.right=recurse(data, root.right)
            return root
        return recurse(data, root)            
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

        #status: correct
        #Analysis: Time O(n); traversing tru each element once
        #Space O(n); storing results
        #ref: 1/13/2023P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day80/80-,0.void-x1pomo(5:30-6:00),1.serialializeAndDeserializeBinaryTreeTimed25Mins-x1pomo(6:00-6:30),2.implement-x2pomo(6:30-7:30),3.courseScheduleTimed25Mins-x1pomo(7:30-8:00),4.implement-x2pomo(8:00-9:00),5.groupAnagramsTimed25Mins-x1pomo(9:00-9:30),6.implement-x2pomo(9:30-10:30),7.findAllAnagramsInAStringTimed25Mins-x1pomo(10:30-11:00),8.absorber-x1pomo(11:00-11:30)=x12pomo(5:30-11:30)delayed(6:00-11:30)
