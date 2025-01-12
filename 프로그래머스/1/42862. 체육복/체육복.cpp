#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve) {
    int answer = n - lost.size();

    for (auto it = lost.begin(); it != lost.end();) {
        auto pos = find(reserve.begin(), reserve.end(), *it);
        if (pos != reserve.end()) {
            reserve.erase(pos);
            it = lost.erase(it);
            answer++;
        } else {
            ++it;
        }
    }

    sort(reserve.begin(), reserve.end());
    sort(lost.begin(), lost.end());

    for (int l : lost) {
        auto pos = find(reserve.begin(), reserve.end(), l - 1);
        if (pos != reserve.end()) {
            reserve.erase(pos);
            answer++;
            continue;
        }

        pos = find(reserve.begin(), reserve.end(), l + 1);
        if (pos != reserve.end()) {
            reserve.erase(pos);
            answer++;
        }
    }
    return answer;
}