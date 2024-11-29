#include <iostream>
#include <vector>
#include <tuple>
#include <algorithm>

using namespace std;
int n;
int answer = 1e9;

vector<int> dx = {0, 0, 1, -1};
vector<int> dy = {1, -1, 0, 0};

void dfs(vector<tuple<int, int>> & vec, vector<vector<int>> & matrix) {
    if (vec.size() == 3) {
        int sum = 0;

        vector<vector<bool>> visited(n, vector<bool>(n, false));
        
        for (tuple<int, int> t : vec) {
            int x = get<0>(t);
            int y = get<1>(t);

            if (visited[x][y]) {
                return;
            }

            visited[x][y] = true;
            sum += matrix[x][y];

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (nx < 0 || nx >= n || ny < 0 || ny >= n || visited[nx][ny]) {
                    return;
                }

                visited[nx][ny] = true;
                sum += matrix[nx][ny];
            }
        }
        answer = min(answer, sum);
        return;
    }

    for (int i = 1; i < n - 1; i++) {
        for (int j = 1; j < n - 1; j++) {
            if (find(vec.begin(), vec.end(), make_tuple(i, j)) != vec.end()) {
                continue;
            }
            vec.push_back({i, j});

            dfs(vec, matrix);

            vec.pop_back();
        }
    }

}
int main() {
    cin >> n;

    vector<vector<int>> matrix(n, vector<int>(n));

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> matrix[i][j];
        }
    }

    vector<vector<bool>> vec(n, vector<bool>(n, false));

    
    for (int i = 1; i < n - 1; i++) {
        vector<tuple<int, int>> temp;
        for (int j = 1; j < n - 1; j++) {
            temp.push_back({i, j});
            dfs(temp, matrix);     
            temp.pop_back();
        }
    }

    cout << answer << endl;
    return 0;
}