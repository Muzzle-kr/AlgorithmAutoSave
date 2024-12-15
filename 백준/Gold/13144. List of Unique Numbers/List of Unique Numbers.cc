#include <iostream>
#include <vector>
#include <map>

using namespace std;

int n;
long long answer = 0;

int main() {
    cin >> n;
    map<int, int> num_map;
    int s = 0;
    int e = 0;

    vector<int> a;
    for (int i = 0; i < n; i++) {
        int num;
        cin >> num;
        a.push_back(num);
    }

    while (e < n) {
        int num = a[e];
        if (num_map[num] == 0) { // 숫자가 윈도우에 없는 경우
            num_map[num]++;
            e++;
            answer += (e - s); // 현재 윈도우 크기를 결과에 추가
        } else { // 중복된 숫자가 발견된 경우
            num_map[a[s]]--; // 시작점을 이동하며 숫자를 제거
            s++;
        }
    }

    cout << answer << endl;
    return 0;
}
