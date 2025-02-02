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

    int total_state = n * m * (k + 1) * 2;
    auto idx = [=](int x, int y, int w, int dn) {
        return ((x * m + y) * ((k + 1) * 2)) + (w * 2 + dn);
    };

    vector<int> visited(total_state, INT_MAX);

    deque<tuple<int, int, int, int>> q;
    q.push_back({0, 0, 0, 0});
    visited[idx(0, 0,0 ,0)] = 1;

    while(!q.empty()) {
        auto [x, y, w, dn] = q.front();

        q.pop_front();

        if (x == n - 1 && y == m - 1) {
            cout << visited[idx(x, y, w, dn)] << endl;
            return 0;
        }

        for (int d = 0; d < 4; d++) {
            int nx = x + dx[d];
            int ny = y + dy[d];


            if (0 <= nx && nx < n && 0 <= ny && ny < m) {
                if (v[nx][ny] == 0) {
                    if (visited[idx(nx, ny, w, 1- dn)] > visited[idx(x, y, w, dn)] + 1) {
                        visited[idx(nx, ny, w, 1- dn)] = visited[idx(x, y, w, dn)] + 1;
                        q.push_back({nx, ny, w,  1 - dn});
                    }
                } else {
                    if (visited[idx(nx, ny, w + 1, 1 - dn)] > visited[idx(x, y, w, dn)] + 1) {
                        // 낮일 경우 벽을 부수고 갈 수 있음
                        if (!dn) {
                            if (w < k) {
                                visited[idx(nx, ny, w + 1, 1 - dn)] = visited[idx(x, y, w, dn)] + 1;
                                q.push_back({nx, ny, w + 1, 1 - dn});
                            }
                        // 밤일 경우 기다린다.
                        } else {
                            visited[idx(x, y, w, 1 - dn)] = visited[idx(x, y, w, dn)] + 1;
                            q.push_back({x, y, w, 1 - dn});
                        }
                    }
                }
            }
        }
    }
    cout << -1 << endl;
    return 0;
}
