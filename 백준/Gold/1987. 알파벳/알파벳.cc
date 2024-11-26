#include <iostream>
#include <vector>
#include <string>

using namespace std;

int n, m;
vector<int> dx = {0, 0, 1, -1};
vector<int> dy = {1, -1, 0, 0};

int answer = 0;

vector<vector<char>> matrix(20, vector<char>(20));
vector<bool> a_visited(26, false);

void dfs(int x, int y, int count) {
    bool canGo = false;

    for (int i = 0; i < 4; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];

        if (nx >= 0 && nx < n && ny >= 0 && ny < m) {
            int n_number = matrix[nx][ny] - 'A';

            if (!a_visited[n_number]) {
                canGo = true;   
                a_visited[n_number] = true;

                dfs(nx, ny, count + 1);

                a_visited[n_number] = false;
            }
        }
    }

    if (!canGo) {
        answer = max(answer, count);
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n >> m;
    cin.ignore();

    for (int i = 0; i < n; i++) {
        string line;
        getline(cin, line);

        for (int j = 0; j < m; j++) {
            matrix[i][j] = line[j];
        }
    }

    a_visited[matrix[0][0] - 'A'] = true;
    dfs(0, 0, 1);

    cout << answer << '\n';
    return 0;
}