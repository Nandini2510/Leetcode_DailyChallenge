class Solution {
public:
    void dfs(vector<vector<int>>& grid,vector<vector<int>> &vis,int i, int j, int m, int n, int &ans){
       if( i < 0 || j < 0 || i >= m || j >= n || grid[i][j] == 0){
           ans++;
           return;
       }
       if(vis[i][j] == 1){
           return;
       }
       vis[i][j] = 1;
        dfs(grid, vis, i + 1, j, m, n, ans);
        dfs(grid, vis, i - 1, j, m, n,ans);
        dfs(grid, vis, i, j + 1, m, n, ans);
        dfs(grid, vis, i, j - 1, m, n, ans);
    }
    int islandPerimeter(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        int ans = 0;
        vector<vector<int>> vis(m, vector<int>(n,0));
        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                if( grid[i][j] == 1){
                    dfs(grid,vis, i, j, m, n, ans);
                }
            }
        }
        return ans;
    }
};