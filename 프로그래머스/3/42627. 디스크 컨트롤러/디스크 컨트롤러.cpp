#include <vector>
#include <tuple>
#include <queue>
#include <algorithm>
using namespace std;
struct cmp {
    bool operator() (tuple<int, int, int> a, tuple<int, int, int> b) {
        if (get<0>(a) != get<0>(b)) {
            return get<0>(a) > get<0>(b);
        }

        if (get<1>(a) != get<1>(b)) {
            return get<1>(a) > get<1>(b);
        }

        return get<2>(a) > get<2>(b);
    }
};
int solution(vector<vector<int>> jobs) {
    int answer = 0;
    priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, cmp> pq;

    sort(jobs.begin(), jobs.end());
    int completed_jobs = 0;
    int idx = 0;
    int current_time = 0;

    while (completed_jobs < jobs.size()) {
        while (idx < jobs.size() && jobs[idx][0] <= current_time) {
            pq.push({jobs[idx][1], jobs[idx][0], idx});
            idx++;
        }

        if (!pq.empty()) {
            // 큐에서 가장 우선순위가 높은 작업 처리
            auto t = pq.top();
            pq.pop();
            int lead_time = get<0>(t);
            int request_time = get<1>(t);
            

            current_time += lead_time; // 현재 시간 업데이트
            answer += current_time - request_time; // 대기 시간 계산
            completed_jobs++;
        } else {
            // 처리할 작업이 없으면 현재 시간을 다음 요청 시간으로 이동
            current_time = jobs[idx][0];
        }
    }
    return answer / jobs.size();
}