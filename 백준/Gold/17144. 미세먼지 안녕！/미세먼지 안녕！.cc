#include <iostream>
#include <vector>
#include <tuple>

using namespace std;

int r, c, t;
vector<tuple<int, int>> air_cleaner;
vector<int> dx = { -1, 0, 1, 0 };
vector<int> dy = { 0, 1, 0, -1 };

bool is_air_cleaner_coordinates(int x, int y) {
    for (auto [ax, ay] : air_cleaner) {
        if (x == ax && y == ay) {
            return true;
        }
    }
    return false;
}

void work_air_cleaner_bottom(vector<vector<int>>& matrix, int x, int y) {
    // 공기청정기 하단 순환
    for (int i = x + 1; i < r - 1; i++) matrix[i][y] = matrix[i + 1][y];
    for (int i = y; i < c - 1; i++) matrix[r - 1][i] = matrix[r - 1][i + 1];
    for (int i = r - 1; i > x; i--) matrix[i][c - 1] = matrix[i - 1][c - 1];
    for (int i = c - 1; i > y + 1; i--) matrix[x][i] = matrix[x][i - 1];
    matrix[x][y + 1] = 0;
}

void work_air_cleaner_top(vector<vector<int>>& matrix, int x, int y) {
    // 공기청정기 상단 순환
    for (int i = x - 1; i > 0; i--) matrix[i][y] = matrix[i - 1][y];
    for (int i = y; i < c - 1; i++) matrix[0][i] = matrix[0][i + 1];
    for (int i = 0; i < x; i++) matrix[i][c - 1] = matrix[i + 1][c - 1];
    for (int i = c - 1; i > y + 1; i--) matrix[x][i] = matrix[x][i - 1];
    matrix[x][y + 1] = 0;
}

void spread_fine_dust(vector<vector<int>>& matrix) {
    vector<vector<int>> tmp_matrix(r, vector<int>(c, 0));

    for (int x = 0; x < r; x++) {
        for (int y = 0; y < c; y++) {
            if (matrix[x][y] > 0) {
                int spread_amount = matrix[x][y] / 5;
                int total_spread = 0;

                for (int i = 0; i < 4; i++) {
                    int nx = x + dx[i];
                    int ny = y + dy[i];

                    if (nx >= 0 && nx < r && ny >= 0 && ny < c && !is_air_cleaner_coordinates(nx, ny)) {
                        tmp_matrix[nx][ny] += spread_amount;
                        total_spread += spread_amount;
                    }
                }
                matrix[x][y] -= total_spread;
            }
        }
    }

    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            matrix[i][j] += tmp_matrix[i][j];
        }
    }
}

int main() {
    cin >> r >> c >> t;
    vector<vector<int>> matrix(r, vector<int>(c));

    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            cin >> matrix[i][j];
            if (matrix[i][j] == -1) {
                air_cleaner.push_back(make_tuple(i, j));
            }
        }
    }

    while (t--) {
        spread_fine_dust(matrix);
        work_air_cleaner_top(matrix, get<0>(air_cleaner[0]), get<1>(air_cleaner[0]));
        work_air_cleaner_bottom(matrix, get<0>(air_cleaner[1]), get<1>(air_cleaner[1]));
    }

    int answer = 0;
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            if (matrix[i][j] > 0) answer += matrix[i][j];
        }
    }

    cout << answer << endl;
    return 0;
}
