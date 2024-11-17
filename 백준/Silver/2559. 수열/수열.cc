#include <iostream>
#include <vector>
#include <climits> // INT_MIN

using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    vector<int> arr(n);

    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    int result = INT_MIN; // 최대 합 초기화
    int current_sum = 0;

    // 초기 윈도우 합 계산
    for (int i = 0; i < m; i++) {
        current_sum += arr[i];
    }
    result = current_sum;

    // 슬라이딩 윈도우로 최대 합 계산
    for (int i = m; i < n; i++) {
        current_sum += arr[i] - arr[i - m]; // 새 값을 추가하고 첫 값을 제거
        result = max(result, current_sum); // 최대값 갱신
    }

    cout << result << endl;
    return 0;
}
