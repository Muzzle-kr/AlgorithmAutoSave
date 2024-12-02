#include <iostream>
#include <vector>

using namespace std;

int r, c;
vector<int> a_arr(26, 0);

vector<int> dx = {0, 0, 1, -1};
vector<int> dy = {1, -1, 0, 0};

int answer = 0;

void dfs(int x, int y, int count, auto & matrix) {
    answer = max(answer, count);

    for (int i = 0; i < 4; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];

        if (nx >= 0 && nx < r && ny >= 0 && ny < c) {
            char alpha = matrix[nx][ny];
            if (!a_arr[alpha - 65]) {
                a_arr[alpha - 65] = 1;
                dfs(nx, ny, count + 1, matrix);
                a_arr[alpha - 65] = 0;
            }
        }
    }
}

int main() {
    cin >> r >> c;
    cin.ignore();

    vector<vector<char>> matrix(r, vector<char>(c));

    for (int i = 0; i < r; i++) {
        string line;
        getline(cin, line);

        for (int j = 0; j < c; j++) {
            matrix[i][j] = line[j];
        }
    }
    a_arr[matrix[0][0] - 65] = 1;
    dfs(0, 0, 1, matrix);
    cout << answer << endl;

    return 0;
}
