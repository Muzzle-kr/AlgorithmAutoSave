// # 1.성에있는 방의 개수
// # 2. 가장 넓은 방의 넓이
// # 3. 하나의 벽을 제거하고 얻을 수 있는 가장 넓은 방의 크기
// https://www.acmicpc.net/problem/2234
// 서쪽에 벽이 있을 때는 1을, 북쪽에 벽이 있을 때는 2를, 동쪽에 벽이 있을 때는 4를, 남쪽에 벽이 있을 때는 8
#include <iostream>
#include <vector>
#include <bitset>
#include <cmath>

using namespace std;
typedef vector<vector<bool>> vvb;
typedef vector<vector<int>> vvi;

int n, m;
vector<int> dx = {0, -1, 0, 1};
vector<int> dy = {-1, 0, 1, 0};

int largest_room = 0;

int dfs(int x, int y, vvi& matrix, vvb& visited) {
    int count = 1;
    visited[x][y] = true;
    bitset<4> bin = (matrix[x][y]);

    for (int i = 0; i < 4; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];

        // 범위를 벗어나면 continue
        if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
        
        
        // 해당 방향에 벽이 있으면 continue
        if (bin[i] == 1) continue;

        // 이미 방문한 경우 continue
        if (visited[nx][ny]) continue;

        count += dfs(nx, ny, matrix, visited);
    }    

    return count;
}

int main() {
    cin >> m >> n;

    vvi matrix(n, vector<int>(m));

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> matrix[i][j];
        }
    }

    
    int room_count = 0;

    vvb visited(n, vector<bool>(m, false));

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (visited[i][j]) continue;
            largest_room = max(largest_room, dfs(i, j, matrix, visited));
            room_count++;   
        }
    }

    int final_largest_room = largest_room;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            bitset<4> bin (matrix[i][j]);

            vvb visited(n, vector<bool>(m, false));

            for (int k = 0; k < 4; k++) {
                if (bin[k] == 1) {
                    // k번째 방향의 벽을 다시 치기
                    matrix[i][j] -= (1 << k);
                    final_largest_room = max(final_largest_room, dfs(i, j, matrix, visited));
                    matrix[i][j] += (1 << k);
                };
            }
        }
    }

    cout << room_count << endl;
    cout << largest_room << endl;
    cout << final_largest_room << endl;
    return 0;
}