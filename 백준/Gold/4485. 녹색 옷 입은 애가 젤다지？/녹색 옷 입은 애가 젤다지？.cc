#include <iostream>
#include <vector>
#include <queue>
#include <tuple>

using namespace std;
int main() {

    vector<int> dx = {0, 0, 1, -1};
    vector<int> dy = {1, -1, 0, 0};

    int index = 1;
    while (true) {
        int n;
        cin >> n;

        if (n == 0) {
            break;
        }

        vector<vector<int>> v(n, vector<int>(n, 0));

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                cin >> v[i][j];
            }
        }

        priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<tuple<int, int, int>>> pq;
        vector<vector<int>> dist(n, vector<int>(n, 1e9));
        dist[0][0] = v[0][0];
        pq.push({v[0][0], 0, 0});

        while (!pq.empty()) {
            auto [d, x, y] = pq.top();
            pq.pop();

            if (dist[x][y] < d) {
                continue;
            }

            if (x == n - 1 && y == n - 1) {
                cout << "Problem " << index << ": " << d << '\n';
                break;
            }

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (nx < 0 || nx >= n || ny < 0 || ny >= n) {
                    continue;
                }

                if (dist[nx][ny] > dist[x][y] + v[nx][ny]) {
                    dist[nx][ny] = dist[x][y] + v[nx][ny];
                    pq.push({dist[nx][ny], nx, ny});
                }
            }
        }

        index++;
    }
    return 0;
}