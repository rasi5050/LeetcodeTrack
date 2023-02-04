# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca=None
        def recurse(root):
            nonlocal lca
            if not root:
                return False

            left,right=recurse(root.left), recurse(root.right)
           
            curr = root==p or root==q
            if curr+left+right>=2:
                lca=root
            return curr or left or right
        recurse(root)
        return lca
    
    #status: correct; help(https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/solution/) - approach 1
    #Analysis: Time O(n), Space O(1)
    #ref: 2/4/2023P2:track1-cpGrind75;Day101/102;doLeetcodeBlind75-3q/day-14/45Q:completeOn2/15/2023-Day7/15:prepareTiktokDevOpsIntenseFocusDay2/7;1.BasicCalculator3TImed25Mins-x1pomo(6:00-6:30),2.implement-x2pomo(6:30-7:30),3.longestIncreasingPathInAMatrixTimed25Mins-x1pomo(7:30-8:00),4.implement-x1pomo(8:00-8:30),5.mergeIntervalsTimed25Mins-x1pomo(8:30-9:00),6.decodeStringTimed25Mins-x1pomo(9:00-9:30),7.implement-x2pomo(9:30-10:30),8.absorber-x1pomo(10:30-11:00)-x12pomo(5:30-11:30)alter-x10pomo(6:00-11:00)
