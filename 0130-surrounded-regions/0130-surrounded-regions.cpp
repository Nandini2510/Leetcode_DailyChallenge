class Solution {
public:
    void dfs(vector<vector<char>>& board,vector<vector<int>> &vis, int i, int j, int m, int n){
        if(i < 0 || j < 0 || i >= m || j >= n || board[i][j] == 'X' || vis[i][j]){
            return;
        }
        vis[i][j] = 1;
        dfs(board, vis, i+1, j, m, n);
        dfs(board, vis, i-1, j, m, n);
        dfs(board, vis, i, j + 1, m, n);
        dfs(board, vis, i, j - 1, m, n);
    }
    void solve(vector<vector<char>>& board) {
        int m = board.size();
        int n = board[0].size();
        vector<vector<int>> vis(m, vector<int>(n,0));
        for(int i=0; i<m; i++){
            for(int j = 0; j < n ; j++){
                if(i == 0 || j == 0 || i == m - 1 || j == n - 1){
                    if(board[i][j] == 'O' && !vis[i][j]){
                    dfs(board, vis, i, j, m, n);
                }
                }
                
            }
            
        }
        for(int i=0; i<m ; i++){
            for(int j = 0; j < n ; j++){
                if(board[i][j] == 'O' && vis[i][j] == 0){
                    board[i][j] = 'X';
                }
            }
            
        }
    }
};