class Solution {
    int[][] dirs = new int[][]{{0,1},{0,-1},{1,0},{-1,0}};

    public int dfs(int i, int j, boolean[][] visited, int[][] grid){
        if(i<0 || i>=grid.length || j<0 || j>=grid[0].length || grid[i][j]==0 || visited[i][j])
            return 0;
        visited[i][j] = true;
        int area = 1;
        for(int[] dir: dirs){
            area += dfs(i+dir[0], j+dir[1], visited, grid);
        }
        return area;
    }
    public int maxAreaOfIsland(int[][] grid) {
        int m=grid.length, n=grid[0].length;
        int maxArea=0;
        boolean[][] visited = new boolean[m][n];
        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                if(grid[i][j]==1 && !visited[i][j]){
                    maxArea = Math.max(maxArea, dfs(i,j,visited,grid));
                }
            }
        }
        return maxArea;
    }
}