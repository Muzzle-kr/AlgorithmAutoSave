// 5 17

#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int n, m;
int MAX = 100000;
vector<int> visited(MAX + 1, -1);
vector<int> ways(MAX + 1, 0);    

int main() {
    cin >> n >> m;
    queue<tuple<int, int>> q;
    visited[n] = 0;
    ways[n] = 1;
    q.push({n, 0});

    while (!q.empty()) {
        auto [x, time] = q.front();
        q.pop();

        vector<int> next_position = {x - 1, x + 1, x * 2};

        for (int next : next_position) {
            if (next < 0 || next > MAX) continue;

            if (visited[next] == -1) {
                visited[next] = time + 1;
                ways[next] = ways[x];
                q.push({next, time + 1});
            } else if (visited[next] == time + 1) {
                ways[next] += ways[x];
            }
        }
    }

    cout << visited[m] << endl;
    cout << ways[m] << endl;
    return 0;
}