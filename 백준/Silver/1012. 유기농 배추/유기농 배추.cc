#include <iostream>
#include <vector>
#include <queue>
#include <tuple>

using namespace std;
typedef vector<vector<int>> vvi;

int dx[] = {0, 0, -1, 1};
int dy[] = {-1, 1, 0, 0};

void bfs(const vvi& maze, int n, int m, int startX, int startY, vvi& visited) {
    queue<tuple<int, int>> q;
    q.push({startX, startY});
    visited[startX][startY] = 1;

    while(!q.empty()) {
        int x, y;
        tie(x, y) = q.front();
        q.pop();

        for (int k = 0; k < 4; k++) {
            int nx = x + dx[k];
            int ny = y + dy[k];

            if (0 <= nx && nx < n && 0 <= ny && ny < m && maze[nx][ny] == 1 && !visited[nx][ny]) {
                visited[nx][ny] = 1;
                q.push({nx, ny});
            }
        }
    }
}

int cabbage(int n, int m, int k) {
    vvi v(n, vector<int>(m, 0));

    for (int i = 0; i < k; i++) {
        int x, y;
        cin >> x >> y;
        v[x][y] = 1;
    }

    vvi visited(n, vector<int>(m, 0));
    int result = 0;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (v[i][j] == 1 && !visited[i][j]) {
                visited[i][j] = 1;
                bfs(v, n, m, i, j, visited);
                result += 1;
            }
        }
    }
    return result;
}
int main() {
    int t;
    cin >> t;

    for (int i = 0; i < t; i++) {
        int n, m, k;
        cin >> n >> m >> k;

        int result = cabbage(n, m, k);
        cout << result << '\n';
    }

}
