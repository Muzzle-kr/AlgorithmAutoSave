#include <iostream>
#include <vector>
#include <tuple>
#include <queue>

using namespace std;

vector<int> dx = {0, 0, 1, -1};
vector<int> dy = {1, -1, 0, 0};

int bfs(vector<vector<int>> &graph) {
    int n = graph.size();
    int m = graph[0].size();
    vector<vector<bool>> visited(n, vector<bool>(m, false));
    queue<tuple<int, int, int>> q;
    q.push({0, 0, 0});
    visited[0][0] = true;

    while (!q.empty()) {
        auto [x, y, c] = q.front();
        q.pop();

        if (x == n - 1 && y == m - 1) {
            return c + 1;
        }

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx < 0 || nx >= n || ny < 0 || ny >= m || visited[nx][ny] || graph[nx][ny] != 1) continue;
            visited[nx][ny] = true;
            q.push({nx, ny, c + 1});
        }
    }
    return 0;
}

int main() {
    int n, m;
    cin >> n >> m;
    vector<vector<int>> matrix(n, vector<int>(m));

    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        for (int j = 0; j < m; j++) {
            matrix[i][j] = s[j] - '0';
        }
    }

    int result = bfs(matrix);
    cout << result << endl;
    return 0;
}
