class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root==None:
            return []
        if root:
            return [root.val]+self.preorderTraversal(root.left)+self.preorderTraversal(root.right)
