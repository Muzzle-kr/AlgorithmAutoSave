#include <iostream>
#include <vector>
#include <queue>
#include <tuple>

using namespace std;
int n, m, x;
typedef vector<vector<pair<int, int>>> graph;

int dijkstra(int s, int e, graph & g) {
    vector<int> distance(n + 1, 1e9);
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;

    pq.push({0, s});
    distance[s] = 0;

    while (!pq.empty()) {
        auto [current_dist, current_node] = pq.top();
        pq.pop();

        if (current_dist > distance[current_node]) continue;

        for (auto [next_node, weight] : g[current_node]) {
            int new_dist = current_dist + weight;
            if (new_dist < distance[next_node]) {
                distance[next_node] = new_dist;
                pq.push({new_dist, next_node});
            }
        }
    }

    return distance[e];
}


int main() {
    cin >> n >> m >> x;
    
    graph g(n + 1);
    for (int i = 0; i < m; i++) {
        int a, b, t;
        cin >> a >> b >> t;
        g[a].push_back({b, t});
    }

    int answer = 0;
    
    for (int i = 1; i <= n; i++) {
        int go = dijkstra(i, x, g);
        int back = dijkstra(x, i, g);

        answer = max(answer, go + back);
    }
    cout << answer << endl;
    return 0;   
}