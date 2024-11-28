#include <iostream>
#include <queue>
#include <tuple>
#include <vector>

using namespace std;

int n, m;
int sx, sy;
int ex, ey;

vector<int> dx = {0, 0, 1, -1};
vector<int> dy = {1, -1, 0, 0};

struct Compare {
    bool operator()(const tuple<int, int, int>& a, const tuple<int, int, int>& b) {
        return get<2>(a) > get<2>(b); // 3번째 요소 기준 오름차순
    }
};

int main() {
    cin >> n >> m;
    cin >> sx >> sy >> ex >> ey;
    cin.ignore();

    sx -= 1;
    sy -= 1;
    ex -= 1;
    ey -= 1;

    vector<vector<char>> matrix(n, vector<char>(m));
    vector<vector<bool>> visited(n, vector<bool>(m, false));

    for (int i = 0; i < n; i++) {
        string line;
        getline(cin, line);

        for (int j = 0; j < m; j++) {
            matrix[i][j] = line[j];
        }
    }

    priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, Compare> pq;

    pq.push({sx, sy, 0});
    visited[sx][sy] = true;

    while (!pq.empty()) {
        auto [x, y, count] = pq.top();
        pq.pop();

        if (x == ex && y == ey) {
            cout << count << endl;
            break;
        }

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            while (nx >= 0 && nx < n && ny >= 0 && ny < m && matrix[nx][ny] == '0' && !visited[nx][ny]) {
                visited[nx][ny] = true;
                pq.push({nx, ny, count});

                nx += dx[i];
                ny += dy[i];
            }

            // 다음 좌표가 배열 범위를 벗어나지 않고 유효한 경우 처리
            if (nx >= 0 && nx < n && ny >= 0 && ny < m && !visited[nx][ny]) {
                matrix[nx][ny] = '0'; // 방문 표시
                visited[nx][ny] = true;
                pq.push({nx, ny, count + 1});
            }
        }
    }

    return 0;
}
