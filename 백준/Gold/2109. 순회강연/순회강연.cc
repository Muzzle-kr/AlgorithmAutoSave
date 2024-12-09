#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

struct Lecture {
    int pay;
    int day;
};

bool compare(const Lecture& a, const Lecture& b) {
    return a.day < b.day;
}

int main() {
    int n;
    cin >> n;

    vector<Lecture> lectures(n);
    
    for (int i = 0; i < n; i++) {
        cin >> lectures[i].pay >> lectures[i].day;
    }

    sort(lectures.begin(), lectures.end(), compare);

    priority_queue<int, vector<int>, greater<int>> pq;

    for (const auto& lecture : lectures) {
        pq.push(lecture.pay);

        if (pq.size() > lecture.day) {
            pq.pop();
        }
    }

    int maxProfit = 0;
    while (!pq.empty()) {
        maxProfit += pq.top();
        pq.pop();
    }

    cout << maxProfit << endl;

    return 0;
}
