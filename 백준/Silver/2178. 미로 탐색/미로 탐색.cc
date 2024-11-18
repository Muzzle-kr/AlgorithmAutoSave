#include <iostream>
#include <vector>
#include <queue>
#include <tuple>

using namespace std;
typedef vector<vector<int>> vvi;

int dx[] = {0, 0, -1, 1};
int dy[] = {-1, 1, 0, 0};

int bfs(const vvi maze, int n, int m) {
    vvi visited(n, vector<int>(m, 0));
    queue<tuple<int, int, int>> q;

    q.push({0, 0, 1});
    visited[0][0] = 1;

    while(!q.empty()) {
        int x, y, dist;
        tie(x, y, dist) = q.front();
        q.pop();

        if (x == n - 1 && y == m - 1) {
            return dist;
        }

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (0 <= nx && nx < n && 0 <= ny && ny < m && maze[nx][ny] == 1 && !visited[nx][ny]) {
                visited[nx][ny] = 1;
                q.push({nx, ny, dist + 1});
            }
        }
    }
    return -1;
}

int main() {
    int n, m;
    cin >> n >> m;
    vvi v(n, vector<int>(m));

    for (int i = 0; i < n; i++) {
        string row;
        cin >> row;

        for (int j = 0; j < m; j++) {
            v[i][j] = row[j] - '0';
        }
    }

    int result = bfs(v, n, m);
    cout << result << "\n";
    return 0;
}
