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