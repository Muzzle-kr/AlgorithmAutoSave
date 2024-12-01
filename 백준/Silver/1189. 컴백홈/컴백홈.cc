#include <iostream>
#include <vector>

using namespace std;

int n, m, k;
int answer = 0;

vector<int> dx = {0, 0, 1, -1};
vector<int> dy = {1, -1, 0, 0};

void dfs(int x, int y, int count, vector<vector<bool>> & visited, const vector<vector<char>> & matrix) {
   if (count == k) {
       if (x == 0 && y == m - 1 ) {
           answer += 1;
       }
       return;
   }

    for (int k = 0; k < 4; ++k) {
        int nx = x + dx[k];
        int ny = y + dy[k];

        if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
        if (!visited[nx][ny] && matrix[nx][ny] == '.') {
            // if (count + 1 == k && (nx != 0 || ny != m - 1)) continue;
            visited[nx][ny] = true;
            dfs(nx, ny, count + 1, visited, matrix);
            visited[nx][ny] = false;
        }
    }
}

int main() {
    cin >> n >> m >> k;
    vector<vector<char>> matrix(n, vector<char>(m));

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> matrix[i][j];
        }
    }

    vector<vector<bool>> visited(n, vector<bool>(m, false));

    visited[n-1][0] = true;
    dfs(n-1, 0, 1, visited, matrix);

    cout << answer << endl;
    return 0;
}
