#include <iostream>
#include <vector>
#include <sstream>
#include <queue>
#include <tuple>

using namespace std;
int n, m;
int result;
typedef vector<vector<char>> matrix;
typedef vector<vector<int>> vvi;

vector<int> dx = {0, 0, 1, -1};
vector<int> dy = {1, -1, 0, 0};
vector<pair<int, int>> lands;

bool valid_coordinate(int x, int y) {
    return 0 <= x && x < n && 0 <= y && y < m;
}
tuple<int, pair<int, int>> bfs(int x, int y, matrix & v) {
    vvi visited(n, vector<int>(m, 0));
    queue<tuple<int, int, int>> q;
    q.push({x, y, 0});
    visited[x][y] = 1;
    
    int max_count = 0;
    pair<int, int> last_coord;

    while (!q.empty()) {
        auto [cx, cy, count] = q.front();
        q.pop();

        if (count > max_count) {
            max_count = count;
            last_coord = {cx, cy};
        }

        for (int i = 0; i < 4; i++) {
            int nx = cx + dx[i];
            int ny = cy + dy[i];

            
            if (valid_coordinate(nx, ny) && !visited[nx][ny] && v[nx][ny] == 'L') {
                visited[nx][ny] = 1;
                q.push({nx, ny, count + 1});
            }
        }
    }

    return {max_count, last_coord};
}

int main() {    
    cin >> n >> m;
    cin.ignore();

    matrix v(n, vector<char>(m));

    for (int i = 0; i < n; i++) {
        string line;
        getline(cin, line);

        for(int j = 0; j < m; j++) {
            char c = line[j];
            v[i][j] = c;

            if (c == 'L') {
                lands.push_back({i, j});
            }
        }
    }

    int maximum_count;
    pair<int, int> maximum_coordi;

    for(pair<int, int> land : lands) {
        int x = land.first;
        int y = land.second;
        auto [mc, lc] = bfs(x, y, v);

        if (mc > maximum_count) {
            maximum_count = mc;
            maximum_coordi = lc;
        }    
    }

    auto [result, coordi] = bfs(maximum_coordi.first, maximum_coordi.second, v);

    cout << result << endl;
    
    return 0;
}

