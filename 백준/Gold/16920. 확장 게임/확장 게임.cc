#include <iostream>
#include <deque>
#include <queue>
#include <tuple>
#include <vector>
#include <sstream>

using namespace std;

vector<int> dx = {0, 0, 1, -1};
vector<int> dy = {1, -1, 0, 0};

int main() {
    int n, m, a;

    cin >> n >> m >> a;

    vector<int> s(a);

    for (int i = 0; i < a; i++) {
        cin >> s[i];
    }

    vector<vector<tuple<int, int>>> coordinates(a);
    vector<vector<string>> matrix(n, vector<string>(m, "."));
    
    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;

        for (int j = 0; j < m; j++) {
            char c = s[j];

            if (isdigit(c)) {
                coordinates[c - '0' - 1].push_back({i, j});
            }
            matrix[i][j] = c;
        }
    }

    // coordinates를 순회하면서 점찍기 시작
    while (true) {
        bool is_end = true;

        for (int i = 0; i < coordinates.size(); i++) {
            deque<tuple<int, int, int>> q;
            vector<tuple<int, int>> new_coordi;

            for (const auto cordi : coordinates[i]) {
                auto [x, y] = cordi;
                q.push_back({x, y, 0});
                is_end = false;
            }

            while (!q.empty()) {
                auto [x, y, c] = q.front();
                q.pop_front();
            

                for (int j = 0; j < 4; j++) {
                    int nx = x + dx[j];
                    int ny = y + dy[j];

                    if (nx < 0 || nx >= n || ny < 0 || ny >= m) {
                        continue;
                    }

                    if (matrix[nx][ny] == ".") {
                        matrix[nx][ny] = matrix[x][y];

                        if (c + 1 < s[i]) {
                            q.push_back({nx, ny, c + 1});    
                        } else {
                            new_coordi.push_back({nx, ny});
                        }
                    }
                }
            }

            coordinates[i].clear();
            coordinates[i] = new_coordi;
        }

        if (is_end) {
            break;
        }
    }


    vector<int> answer(a, 0);

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (isdigit(matrix[i][j][0])) {
                answer[stoi(matrix[i][j]) - 1]++;
            }
        }
    }
    
    for (int i = 0; i < a; i++) {
        cout << answer[i] << " ";
    }
    return 0;
}