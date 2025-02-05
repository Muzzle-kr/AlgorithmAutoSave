#include <iostream>
#include <vector>
#include <tuple>
#include <queue>
#include <map>
using namespace std;

vector<int> dx = {0, 0, 1, -1};
vector<int> dy = {1, -1, 0, 0};

int main() {
    int n, m;
    cin >> n >> m;

    map<tuple<int, int>, vector<tuple<int, int>>> switches;

    for (int i = 0; i < m; i++) {
        int x, y, a, b;
        cin >> x >> y >> a >> b;
        switches[{x-1, y-1}].push_back({a-1, b-1});
    }

    vector<vector<bool>> lit(n, vector<bool>(n, false));
    vector<vector<bool>> visited(n, vector<bool>(n, false));

    lit[0][0] = true;
    visited[0][0] = true;
    int answer = 1;

    queue<tuple<int, int>> q;
    q.push({0,0});

    while (!q.empty()) {
        auto [x, y] = q.front();
        q.pop();

        for (auto [sx, sy] : switches[{x, y}]) {
            if(!lit[sx][sy]) {
                lit[sx][sy] = true;
                answer++;

                for (int i = 0; i < 4; i++) {
                    int nx = sx + dx[i];
                    int ny = sy + dy[i];

                    if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;

                    if (visited[nx][ny]) {
                        q.push({nx, ny});
                    }
                }
            }
        }

        for(int i = 0; i < 4; i++){
            int nx = x + dx[i], ny = y + dy[i];
            if(nx < 0 || nx >= n || ny < 0 || ny >= n) continue;

            if(lit[nx][ny] && !visited[nx][ny]) {
                visited[nx][ny] = true;
                q.push({nx,ny});
            }
        }
    }

    cout << answer << endl;
    return 0;
}