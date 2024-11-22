#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;

int dfs(int start, vvi &matrix, vi &visited) {
    int count = 1;
    visited[start] = 1;

    for (int next : matrix[start]) {
        if (!visited[next]) {
            count += dfs(next, matrix, visited);
        }
    }

    return count;
}

int main() {
    int n, m;
    cin >> n >> m;

    vvi matrix(n + 1); // 노드 번호가 1부터 시작한다고 가정

    // 간선 정보 입력
    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        matrix[b].push_back(a); // b를 해킹하면 a도 해킹 가능
    }

    int max_value = 0;
    vi result_array;

    for (int i = 1; i <= n; i++) {
        vi visited(n + 1, 0);
        int result = dfs(i, matrix, visited);

        if (result > max_value) {
            max_value = result;
            result_array.clear();
            result_array.push_back(i);
        } else if (result == max_value) {
            result_array.push_back(i);
        }
    }

    for (int r : result_array) {
        cout << r << " ";
    }
    cout << endl;

    return 0;
}
