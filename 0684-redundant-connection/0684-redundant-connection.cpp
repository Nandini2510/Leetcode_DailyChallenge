class Solution {
public:
    unordered_map<int, vector<int>> adjList;
    bool dfs(int node, int parent,vector<int> &vis){
        vis[node] = 1;
        for(auto it : adjList[node]){
            if(vis[it] == 1 && it != parent){
                return 1;
            }else if(vis[it] == 0 && dfs(it, node, vis) == 1){
                return 1;
            }
        }
        return 0;
    }
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        for(auto it : edges){
            int u = it[0];
            int v = it[1];
            adjList[u].push_back(v);
             adjList[v].push_back(u);
        
        vector<int> vis(edges.size() + 1, 0);
        if(dfs(u, -1,vis) == 1){
            return it;
        }
        }
        return {};
    }
};