// https://leetcode.com/problems/number-of-islands/
// O(rows * cols) time | O(rows * cols)space

class Solution {
    public int numIslands(char[][] grid) {
        int count = 0;
        for (int i=0 ; i<grid.length; i++) {
            for (int j=0 ; j<grid[0].length; j++) {
                if (grid[i][j]=='1') {  // found and island
                    count += 1;
                    callDFS(grid, i, j);
                }
            } 
        }
        return count;
    }
    
    public void callDFS(char[][] grid, int i, int j) {
        if (i<0 || i>=grid.length || j<0 || j>=grid[0].length || grid[i][j]=='0')
            return;  // break if out of bounds or not a piece of land
        grid[i][j]='0';  // mark as seen
        callDFS(grid, i-1, j);  // go up
        callDFS(grid, i+1, j);  // go down
        callDFS(grid, i, j-1);  // go left
        callDFS(grid, i, j+1);  // go right
    }
}
