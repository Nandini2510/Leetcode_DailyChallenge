class Solution {
public:
    void wallsAndGates(vector<vector<int>>& rooms) {
        int m = rooms.size();
        int n = rooms[0].size();
        queue<pair<int,pair<int,int>>> q;
        vector<vector<int>> vis(m, vector<int>(n,0));
        int delR[] = {-1, 0, 1, 0};
        int delC[] = {0,1,0,-1};
        for(int i=0; i<m;i++){
            for(int j = 0; j<n;j++){
                if(rooms[i][j] == 0 && !vis[i][j]){
                    q.push({0, {i,j}});
                    vis[i][j] = 1;
                }
            }
        }
        while(!q.empty()){
            int dist = q.front().first;
            int r = q.front().second.first;
            int c= q.front().second.second;
            q.pop();
            for(int i=0; i<4;i++){
                int nr = r + delR[i];
                int nc = c + delC[i];
                if(nr < 0 || nc < 0 || nr >= m || nc >= n || vis[nr][nc] == 1 ||
                rooms[nr][nc] == -1 || rooms[nr][nc] == 0){
                    continue;
                }
                vis[nr][nc] = 1;
                rooms[nr][nc] = dist + 1;
                q.push({dist + 1, {nr,nc}});
            }
        }
    }
};