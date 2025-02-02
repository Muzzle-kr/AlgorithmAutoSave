#include <iostream>
#include <vector>
#include <deque>
#include <tuple>
#include <iomanip>
#include <climits>

using namespace std;

vector<int> dx = {-1, 1, 0, 0};
vector<int> dy = {0, 0, -1, 1};

int main() {
    int n, m, k;
    cin >> n >> m >> k;

    vector<vector<int>> v(n, vector<int>(m));

    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        for (int j = 0; j < m; j++) {
            v[i][j] = s[j] - '0';
        }
    }

    vector<vector<vector<int>>> visited(n, vector<vector<int>>(m, vector<int>(k + 1, INT_MAX)));
    deque<tuple<int, int, int>> q;
    q.push_back({0, 0, 0});
    visited[0][0][0] = 1;

    while(!q.empty()) {
        auto [x, y, w] = q.front();
        q.pop_front();

        if (x == n - 1 && y == m - 1) {
            cout << visited[x][y][w] << endl;
            return 0;
        }

        for (int d = 0; d < 4; d++) {
            int nx = x + dx[d];
            int ny = y + dy[d];

            if (0 <= nx && nx < n && 0 <= ny && ny < m) {
                if (v[nx][ny] == 0) {
                    if (visited[nx][ny][w] > visited[x][y][w] + 1) {
                        visited[nx][ny][w] = visited[x][y][w] + 1;
                        q.push_back({nx, ny, w});
                    }
                } else {
                    if (w < k && visited[nx][ny][w + 1] > visited[x][y][w] + 1) {
                        visited[nx][ny][w + 1] = visited[x][y][w] + 1;
                        q.push_back({nx, ny, w + 1});
                    }
                }
            }
        }
    }
    cout << -1 << endl;
    return 0;
}
