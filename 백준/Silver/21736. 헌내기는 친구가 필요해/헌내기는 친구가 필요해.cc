#include <iostream>
#include <vector>
#include <queue>
#include <cmath>
using namespace std;
typedef vector<vector<char>> vvc;
typedef vector<vector<bool>> vvb;

vector<int> dx = {0, 0, 1, -1};
vector<int> dy = {1, -1, 0, 0};

int bfs(int sx, int sy, const vvc& matrix) {
    int n = matrix.size();
    int m = matrix[0].size();

    vvb visited(n, vector<bool>(m, false));
    queue<pair<int, int>> q;
    q.push(make_pair(sx, sy));
    visited[sx][sy] = true;

    int ans = 0;

    while (!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx < 0 || nx >= n || ny < 0 || ny >= m || matrix[nx][ny] == 'X' || visited[nx][ny] == true) continue;

            if (matrix[nx][ny] == 'P') ans++;
            q.push(make_pair(nx, ny));
            visited[nx][ny] = true;
        }
    }

    return ans;
};

int main() {
    int n, m;
    cin >> n >> m;

    vector<vector<char>> matrix(n, vector<char>(m));
    int sx, sy;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            char c;
            cin >> c;
            matrix[i][j] = c;

            if (c == 'I') {
                sx = i;
                sy = j;
            }
        }
    }

    int answer = bfs(sx, sy, matrix);

    if (!answer) {
        cout << "TT" << endl;
    } else {
        cout << answer << endl;
    }

    return 0;
}
