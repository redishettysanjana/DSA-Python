class Solution(object):
    def binaryTreePaths(self, root):

        result = []

        def dfs(node, path):

            if not node:
                return

            path = path + str(node.val)

            if node.left is None and node.right is None:
                result.append(path)
                return

            path += "->"

            dfs(node.left, path)
            dfs(node.right, path)

        dfs(root, "")

        return result