# https://leetcode.com/problems/number-of-islands/
# Runtime: 530 ms, faster than 17.28% of Python online submissions for Number of Islands.
# Memory Usage: 28.9 MB, less than 43.49% of Python online submissions for Number of Islands.
# O(rows * cols) time | O(1) space
class Solution(object):
    def numIslands(self, grid):
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":  # found and island
                    count += 1
                    self.callDFS(grid, i, j)
        return count
    
    def callDFS(self, grid, i, j):
        if (i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == "0"):
            return  # break if out of bounds or not a piece of land
        grid[i][j] = "0"  # mark as seen
        self.callDFS(grid, i - 1, j)  # go up
        self.callDFS(grid, i + 1, j)  # go down
        self.callDFS(grid, i, j - 1)  # go left
        self.callDFS(grid, i, j + 1)  # go right
        
