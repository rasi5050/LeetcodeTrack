# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def recurse(preorder, inorder):
            if not preorder:        #inorder not be checked because when preorder is empty inorder will be empty        
                return None
            node=TreeNode(preorder[0])
            
            i=inorder.index(preorder[0])            
            node.left=recurse(preorder[1:i+1], inorder[:i])
            node.right=recurse(preorder[i+1:], inorder[i+1:])
            return node
        return recurse(preorder, inorder)
            
        #storing global inorder indexes doesnt work because, when the preorder is divided and recursed
        #the inorder should also reflect the preorder elements, then only the index will match
        #the inorder list is used as a index finder to the preorder
        
        #status: correct; didnt understand; help(https://www.youtube.com/watch?v=ihj4IQGZ2zc&t=1s)
        #Analysis: Time O(no of nodes), Space O(no. of nodes)
        #ref: 2/17/2023P2:track1-cpGrind75;Day111/112;doLeetcodeBlind75-3q/day-26/45Q:completeOn2/15/2023-Day19/15,collateQuestionPatternIntoCategoriesAndTemplate-Day9/5:(addWordDescriptionOnceProblemIsSolvedDay6/4),1.uniquePathsTimed25Mins-x1pomo(6:00-6:30),2.implement-x1pomo(6:30-7:00),3.constructABinaryTreeFromPreorderAndInorderTraversalTimed25Mins-x1pomo(7:00-7:30),4.implement-x2pomo(7:30-8:30),5.containerWithMostWaterTimed25Mins-x1pomo(8:30-9:00),6.implement-x1pomo(9:00-9:30),7.applyInternship-x6SdeFromGitHubPage-x2pomo(9:30-10:30),8.applyInternship-x3DevOpsFromLinkedIn-x1pomo(10:30-11:00)             -x12pomo(5:30-11:30)alter-x10pomo(6:00-11:00)

        
        