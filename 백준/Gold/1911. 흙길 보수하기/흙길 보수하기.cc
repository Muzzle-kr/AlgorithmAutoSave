#include <iostream>
#include <vector>
#include <queue>
#include <tuple>

using namespace std;
int n, l;

int main() {
    cin >> n >> l;  
    priority_queue<tuple<int, int>> pq;
    
    int last_pos = 0;
    
    for (int i = 0; i < n; i++) {
        int x, y;
        cin >> x >> y;
        pq.push({-x, -y});
    }  
    int answer = 0;

    while (!pq.empty()) {
        auto [start, end] = pq.top();
        pq.pop();
        start = -start;
        end = -end;
        
        if (last_pos >= end) {
            continue;
        }
        
        if (last_pos < start) {
            last_pos = start;
        }
        
        while (last_pos < end) {
            last_pos += l;
            answer++;
        }
    }

    cout << answer << '\n';
    return 0;
}