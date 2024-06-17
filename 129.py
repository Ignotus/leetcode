class Solution:
    def sumTraverse(self, root, stack: list, acc: list):
        stack.append(root.val)

        if root.left is None and root.right is None:
            acc[0] += sum([val * 10 ** i for i, val in enumerate(reversed(stack))])
        else:
            if root.left is not None:
                self.sumTraverse(root.left, stack, acc)

            if root.right is not None:
                self.sumTraverse(root.right, stack, acc)

        stack.pop()

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        acc = [0]
        self.sumTraverse(root, [], acc)
        return acc[0]
