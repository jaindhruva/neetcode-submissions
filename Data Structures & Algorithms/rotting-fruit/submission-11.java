class Solution {
    public int orangesRotting(int[][] grid) {
        Queue<Integer[]> q = new LinkedList<>();
        int[][] dirs = {{1,0},{-1,0},{0,1},{0,-1}};
        int count = 0;
        for(int i=0; i<grid.length; i++){
            for(int j=0; j<grid[0].length; j++){
                if(grid[i][j]==2)
                    q.add(new Integer[]{i,j});
                if(grid[i][j]==1)
                    count++;
                
            }
        }
        if(q.size()==0 && count==0)
            return 0;
        
        int time = 0, rotten_count = 0;
        while(q.size()>0){
            int size = q.size();
            
            // System.out.println(">>>"+time);
            for(int i=0; i<size; i++){
                Integer[] cell = q.poll();
                // System.out.println(cell[0]+" - "+cell[1]);
                if(grid[cell[0]][cell[1]]==1){
                    grid[cell[0]][cell[1]]=2;
                    rotten_count++;
                }
                if(rotten_count == count)
                    return time;
                for(int[] dir : dirs){
                    int x=cell[0]+dir[0], y=cell[1]+dir[1];
                    if( x<0 || x>=grid.length ||
                        y<0 || y>=grid[0].length ||
                        grid[x][y]!=1)
                        continue;
                    q.add(new Integer[]{x,y});
                    // System.out.println(x+","+y);
                }
            }
            time++;
            
        }
        return -1;
    }
}