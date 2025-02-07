#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

vector<int> dfs(vector<vector<int>> &graph, int node, vector<bool> &visited, vector<int>& result) {
    visited[node] = true;

    for (int neighbor : graph[node]) {
        if (!visited[neighbor]) {
            visited[neighbor] = true;
            result.push_back(neighbor);
            dfs(graph, neighbor, visited, result);
        }
    }
    return result;
}
vector<int> bfs(vector<vector<int>> &graph, int node) {
    vector<int> result;
    vector<bool> visited(graph.size() + 4, false);
    queue<int> q;
    q.push(node);
    visited[node] = true;
    result.push_back(node);

    while (!q.empty()) {
        int start = q.front();
        q.pop();

        for (int neighbour : graph[start]) {
            if (!visited[neighbour]) {
                visited[neighbour] = true;
                q.push(neighbour);
                result.push_back(neighbour);
            }
        }
    }
    return result;
}

int main() {
    int n, m, v;
    cin >> n >> m >> v;
    vector<vector<int>> matrix(n + 4, vector<int>());

    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        matrix[a].push_back(b);
        matrix[b].push_back(a);
    }

    for (int i = 1; i <= n; i++) {
        // 오름차순 정렬
        sort(matrix[i].begin(), matrix[i].end());
    }

    vector<bool> dfsVisited(n + 4, false);
    dfsVisited[v] = true;
    vector<int> dfsResult = { v };
    dfs(matrix, v, dfsVisited, dfsResult);
    vector<int> bfsResult = bfs(matrix, v);


    for (int i = 0; i < dfsResult.size(); i++) {
        cout << dfsResult[i] << " ";
    }

    cout << endl;

    for (int i = 0; i < bfsResult.size(); i++) {
        cout << bfsResult[i] << " ";
    }

    cout << endl;
    return 0;
}
