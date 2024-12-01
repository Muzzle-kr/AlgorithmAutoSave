#include <iostream>
#include <vector>
#include <cmath>
#include <tuple>
#include <queue>

using namespace std;
int n, l, r;

vector<int> dx = {0, 0, -1, 1};
vector<int> dy = {-1, 1, 0, 0};
vector<tuple<int, int, int>> shared;

bool bfs(int i, int j, vector<vector<int>>& matrix, vector<vector<bool>>& visited) {
    queue<tuple<int, int, int>> q;
    q.push({i, j, matrix[i][j]});

    vector<tuple<int, int>> shared_temp;
    shared_temp.push_back({i, j});
    visited[i][j] = true;

    while (!q.empty()) {
        auto [x, y, current] = q.front();
        q.pop();


        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx >= 0 && nx < n && ny >= 0 && ny < n && !visited[nx][ny]) {
                int next = matrix[nx][ny];
                int diff = abs(current - next);

                if (diff >= l && diff <= r) {
                    q.push({nx, ny, next});
                    visited[nx][ny] = true;
                    shared_temp.push_back({nx, ny});
                }
            }
        }
    }

    int size = shared_temp.size();
    int total = 0;

    if (shared_temp.size() > 1) {
        for (int i = 0; i < size; i++) {
            auto [x, y] = shared_temp[i];
            total += matrix[x][y];
        }
        int distribution = round(total / size);

        for (auto [x, y] : shared_temp) {
            shared.push_back({x, y, distribution});
        }
        return true;
    }

    return false;
}

int main() {
    cin >> n >> l >> r;
    vector<vector<int>> matrix(n, vector<int>(n, 0));


    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> matrix[i][j];
        }
    }

    int answer = 0;

    while (true) {
        int is_open = 0;

        vector<vector<bool>> visited(n, vector<bool>(n, false));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (!visited[i][j]) {
                    bfs(i, j, matrix, visited);    
                }        
            }
        }

        int shared_size = shared.size();
        if (shared_size > 0) {

            for (auto [x, y, distribution] : shared) {
                matrix[x][y] = distribution;
            }

            shared.clear();
            answer++;
            continue;
        }
        break;
    }
    cout << answer << endl;
    return 0;
}