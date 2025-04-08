
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: list[list[int]]) -> 'Node':
        def quad_tree(x, y, size):
            # check if grid section is uniform
            is_uniform = True
            first_val = grid[x][y]

            for i in range(x, x + size):
                for j in range(y, y + size):
                    if grid[i][j] != first_val:
                        is_uniform = False
                        break
                    if not is_uniform:
                        break
            
            # If uniform, create a leaf node
            if is_uniform:
                return Node(first_val==1, True)

            # Split into four quadrants
            half_size = size // 2
            topLeft = quad_tree(x, y, half_size)
            topRight = quad_tree(x, y + half_size, half_size)
            bottomLeft = quad_tree(x + half_size, y, half_size)
            bottomRight = quad_tree(x+half_size, y+half_size, half_size)

            return Node(True, False, topLeft, topRight, bottomLeft, bottomRight)
        
        return quad_tree(0, 0, len(grid))