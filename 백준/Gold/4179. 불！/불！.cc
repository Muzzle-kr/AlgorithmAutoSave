#include <iostream>
#include <vector>
#include <queue>
#include <tuple>

using namespace std;

int r, c;
typedef vector<vector<char>> matrix;
pair<int, int> jihoon;
vector<pair<int, int>> fires;

vector<int> dx = {0, 0, 1, -1};
vector<int> dy = {1, -1, 0 ,0};

int bfs(matrix &v) {
    queue<tuple<int, int, int>> jq;
    queue<pair<int, int>> fq;

    jq.push({jihoon.first, jihoon.second, 1});

    for (pair<int, int> fire : fires) {
        fq.push(fire);
    }

    while (!jq.empty()) { 
        int f_length = fq.size();

        for (int f = 0; f < f_length; f++) {
            auto [fx, fy] = fq.front();
            fq.pop();

            for (int k = 0; k < 4; k++) {
                int nx = fx + dx[k];
                int ny = fy + dy[k];

                if (nx >= 0 && nx < r && ny >= 0 && ny < c && v[nx][ny] == '.') {
                    v[nx][ny] = 'F';
                    fq.push({nx, ny});
                }
            }
        }

        
        int j_length = jq.size();
        
        for (int j = 0; j < j_length; j++) {
            auto [jx, jy, count] = jq.front();
            jq.pop();

            if (jx == 0 || jx == r - 1 || jy == 0 || jy == c - 1) {
                return count;
            } 
            
            for (int k = 0; k < 4; k++) {
                int nx = jx + dx[k];
                int ny = jy + dy[k];

                if (nx >= 0 && nx < r && ny >= 0 && ny < c && v[nx][ny] == '.') {
                    v[nx][ny] = 'J';
                    jq.push({nx, ny, count + 1});
                }
            }
        }
    }

    return 0;
}
int main() {
    cin >> r >> c;
    matrix v(r, vector<char>(c));
    cin.ignore();

    for (int i = 0; i < r; i++) {
        string line;
        getline(cin, line);

        for(int j = 0; j < c; j++) {
            char a = line[j];
            
            if (a == 'J') {
                jihoon = {i, j};
            } else if (a == 'F') {
                fires.push_back({i, j});
            }

            v[i][j] = a;
        }
    }

    int result = bfs(v);

    if (!result) {
        cout << "IMPOSSIBLE" << '\n';
    } else {
        cout << result << '\n';
    }

    return 0;
}