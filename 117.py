import math

class Solution:
    def tree_to_array(self, root, tree_array: list):
        """ BFS over the tree, O(n) """
        queue = [root]
        root.level = 0

        while len(queue) > 0:
            node = queue.pop(0)
            tree_array.append(node)
            if node.left is not None:
                node.left.level = node.level + 1
                queue.append(node.left)

            if node.right is not None:
                node.right.level = node.level + 1
                queue.append(node.right)

    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root

        tree_array = []
        self.tree_to_array(root, tree_array)
        for i in range(len(tree_array)-1):
            if tree_array[i].level == tree_array[i+1].level:
                tree_array[i].next = tree_array[i+1]

        for t in tree_array:
            del t.level

        return root

