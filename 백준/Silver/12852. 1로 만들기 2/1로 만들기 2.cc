#include <iostream>
#include <vector>
#include <deque>
#include <tuple>

using namespace std;

void bfs(int n) {
    deque<tuple<int, vector<int>>> q;
    vector<int> arr;
    arr.push_back(n);
    q.push_back(make_tuple(n, arr));
    vector<bool> visited(n + 1, false);
    visited[n] = true;

    while (!q.empty()) {
        auto [x, route] = q.front();
        q.pop_front();

        if (x == 1) {
            cout << route.size() - 1 << endl;
            for (int i = 0; i < route.size(); i++) {
                cout << route[i] << " ";
            }
            cout << endl;
            return;
        }
        if (x % 3 == 0 && !visited[x / 3]) {
            visited[x / 3] = true;
            vector<int> new_route = route;
            new_route.push_back(x / 3);
            q.push_back(make_tuple(x / 3, new_route));
        }

        if (x % 2 == 0 && !visited[x / 2]) {
            visited[x / 2] = true;
            vector<int> new_route = route;
            new_route.push_back(x / 2);
            q.push_back(make_tuple(x / 2, new_route));
        }

        if (x - 1 >= 1 && !visited[x - 1]) {
            visited[x - 1] = true;
            vector<int> new_route = route;
            new_route.push_back(x - 1);
            q.push_back(make_tuple(x - 1, new_route));
        }
    }
}
int main() {
    int n;
    cin >> n;
    bfs(n);
    return 0;
}