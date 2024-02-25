class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        vector<pair<int,int>> adj[n+1];
        for(auto time : times){
            adj[time[0]].push_back({time[2], time[1]});
        }
        vector<int> dist(n+1, INT_MAX);
        priority_queue<pair<int,int>,vector<pair<int,int>>, greater<pair<int,int>>> pq;
        dist[k] = 0;
        pq.push({0, k});

        while(!pq.empty()){
            int dst = pq.top().first;
            int node = pq.top().second;
            pq.pop();
            if(dst > dist[node]){
                continue;
            }
            for(int i=0; i< adj[node].size(); i++){
                pair<int,int> edge = adj[node][i];
                int price = edge.first;
                 int neighbor = edge.second;
                 if(dist[neighbor] > dst + price){
                     dist[neighbor] = dst + price;
                     pq.push({dist[neighbor],neighbor});
                 }
            }
        }
        int result = INT_MIN;
        for (int i = 1; i <= n; i++) {
            result = max(result, dist[i]);
        }
        
        if (result == INT_MAX) {
            return -1;
        }
        return result;
    }
};