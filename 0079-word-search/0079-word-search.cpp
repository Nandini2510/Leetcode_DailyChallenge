class Solution {
public:
    bool dfs(vector<vector<char>>& board, string word, int i, int j, int k, int m, int n, vector<vector<int>> &vis)
    {
        if(k == word.size()){
            return true;
        }
        if((i < 0 || i >=m) || (j < 0 || j >= n) || vis[i][j] == 1){
            return false;
        }
        if(board[i][j] != word[k]){
            return false;
        }
        vis[i][j] = 1;
       bool h1 =  dfs(board, word, i + 1, j, k+1, m, n, vis);
       bool h2 =  dfs(board, word, i, j+1, k+1, m, n, vis);
       bool h3 =  dfs(board, word, i-1, j, k+1, m, n, vis);
       bool h4 =  dfs(board, word, i, j-1, k+1, m, n, vis);
       vis[i][j] = 0;
    return h1 || h2 || h3 || h4;
    }
    bool exist(vector<vector<char>>& board, string word) {
        int m = board.size();
        int n = board[0].size();
        int k = 0;
        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                if(board[i][j] == word[k]){
                    vector<vector<int>> vis(m, vector<int>(n,0));
                    if(dfs(board,word,i,j,k,m,n,vis)) return true;
                }
            }
        }
        return false;
    }
};