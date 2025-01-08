#include <ostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <functional>
using namespace std;

int solution(vector<int> scoville, int K) {
    int answer = 0;
    priority_queue<int, vector<int>, greater<int>> pq;

    for (int i = 0; i < scoville.size(); i++) {
        pq.push(scoville[i]);
    }

    while (pq.top() < K) {
        if (pq.size() < 2) {
            answer = -1;
            break;
        }
        
        int s1 = pq.top();
        pq.pop();
        int s2 = pq.top();
        pq.pop();

        int new_scoville = s1 + (s2 * 2);
        
        pq.push(new_scoville);
        answer++;
    }
    return answer;
}