#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>
#include <algorithm>

using namespace std;
const int MAX_INT = 1000000;
int n, m;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> n >> m;

    if (n > m) {
        cout << n - m << '\n';
        for (int i = n; i >= m; i--) {
            cout << i << " ";
        }
        cout << '\n';
        return 0;
    }

    // BFS 큐와 방문 체크
    queue<int> q;
    unordered_map<int, int> visited; // key: 현재 위치, value: 이전 위치

    q.push(n);
    visited[n] = -1;

    while (!q.empty()) {
        int current = q.front();
        q.pop();

        // 목표 지점에 도달한 경우 경로와 거리 출력
        if (current == m) {
            vector<int> path;
            for (int i = m; i != -1; i = visited[i]) {
                path.push_back(i);
            }
            reverse(path.begin(), path.end());

            cout << path.size() - 1 << '\n'; // 거리 출력
            for (int p : path) {
                cout << p << " ";
            }
            cout << '\n';
            return 0;
        }

        vector<int> next_info = {current - 1, current + 1, current * 2};

        for (int next : next_info) {
            if (next < 0 || next > MAX_INT || visited.count(next)) continue;

            visited[next] = current;
            q.push(next);
        }
    }

    return 0;
}
