#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n, m, r;
    cin >> n >> m >> r;

    vector<priority_queue<int, vector<int>, greater<int>>> lines(n + 1);

    for (int i = 0; i < m; i++) {
        int s, e;
        cin >> s >> e;

        lines[s].push(e);
        lines[e].push(s);
    }

    vector<int> visit(n+1, 0);
    queue<int> q;
    q.push(r);
    visit[r] = 1;

    int order = 2;
    stack<int> reverse_nodes;

    while (!q.empty()) {
        int c = q.front();
        q.pop();

        while (!lines[c].empty()) {
            reverse_nodes.push(lines[c].top());
            lines[c].pop();
        }

        while (!reverse_nodes.empty()) {
            int i = reverse_nodes.top();
            reverse_nodes.pop();

            if (visit[i] == 0) {
                visit[i] = order++;
                q.push(i);
            }
        }
    }

    for (int i = 1; i <= n; i++) {
        cout << visit[i] << '\n';
    }

    return 0;
}
