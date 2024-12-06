#include <iostream>
#include <queue>
#include <tuple>
using namespace std;
int n;
priority_queue<tuple<int, int>> pq;

int main() {
    cin >> n;

    for (int i = 0; i < n; i++) {
        int x, y;
        cin >> x >> y;

        pq.push(make_tuple(-x, y));
    }

    int time = 0;

    while (!pq.empty()) {
        auto [x, y] = pq.top();
        x = -x;
        pq.pop();

        if (time < x) {
            time = x;
        };

        time += y;
    }
    cout << time;
    return 0;
}
