class Solution {
public:
    void dfs(int current_element, const vector<vector<int>>& adj, vector<bool>& visited) {
        visited[current_element] = true;
        for (int neighbor : adj[current_element]) {
            if (!visited[neighbor]) {
                dfs(neighbor, adj, visited);
            }
        }
    }

    int makeConnected(int n, vector<vector<int>>& connections) {
        int len_connections = connections.size();
        if (len_connections < n - 1) {
            return -1;
        }
        // Convert to adj list
        vector<vector<int>> adj(n);
        for (const auto& edge: connections) {
            adj[edge[0]].push_back(edge[1]);
            adj[edge[1]].push_back(edge[0]);
        }

        int counter = 0;
        vector<bool> visited(n, false);

        for (int i = 0; i < n; ++i) {
            if (!visited[i]) {
                counter++;
                dfs(i, adj, visited);
            }
        }

        return counter-1;
    }
};
