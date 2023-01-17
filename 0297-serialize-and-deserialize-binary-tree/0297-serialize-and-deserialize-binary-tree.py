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
        if not root:
            return '_;'
        return '' + str(root.val) + ';' + str(self.serialize(root.left)) + str(self.serialize(root.right))
        
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        i=0
        root=TreeNode()
        def decode(root):
            nonlocal i
            if data[i]=='_':
                i+=2
                return None
            else:
                num=''
                while data[i].isdigit() or data[i]=='-':        #accounting for -ve numbers
                    num+=data[i]
                    i+=1
                i+=1
                root=TreeNode(num)
                root.left=decode(root.left)
                root.right=decode(root.right)
            return root
        return decode(root)
                    
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))