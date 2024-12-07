#include <iostream>
#include <queue>
#include <tuple>
using namespace std;

int main() {
    int n;
    cin >> n;
    priority_queue<tuple<int, int>> pq;

    for (int i = 0; i < n; i++) {
        int t, k;
        cin >> t >> k;
        pq.push({-k, -t});
    }

    int time = 0;
    int answer = 0;
    while (!pq.empty()) {
        auto [end, start] = pq.top();
        pq.pop();

        start = -start;
        end = -end;
        if (time <= start) {
            // cout << start << "에는 회의가 가능합니다." << endl;
            time = end;
            answer += 1;
        }
    }
    cout << answer << endl;
    return 0;
}
